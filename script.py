'''https://github.com/grokdesigns/markdown-mimic'''

import os
import re
import base64
import logging
from github import Github
from github.GithubException import GithubException
from github.InputGitAuthor import InputGitAuthor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Markers for content replacement
START_COMMENT = '<!--MIMIC_START-->'
END_COMMENT = '<!--MIMIC_END-->'
CONTENT_PATTERN = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"

# Getting inputs from environment variables
token = os.environ['INPUT_TOKEN']
repository = os.environ['INPUT_REPOSITORY']
copy_file_location = os.environ['INPUT_SOURCE']
paste_file_location = os.environ['INPUT_TARGET']
branch = os.environ['INPUT_BRANCH']  # Get branch from environment variables

COMMITTER_NAME = "github-actions[bot]"
COMMITTER_EMAIL = "github-actions[bot]@users.noreply.github.com"

def decode_content(encoded_content):
    """Decode base64 encoded content from GitHub"""
    decoded_bytes = base64.b64decode(encoded_content)
    return decoded_bytes.decode('utf-8')

def generate_new_content(source_content, target_content):
    """Generate new content by replacing the marked section"""
    replacement = f"{START_COMMENT}\n{source_content}\n{END_COMMENT}"
    return re.sub(CONTENT_PATTERN, replacement, target_content)

def update_file(repo, file_path, content, message, sha, branch):
    """Update a file in the repository using the specified branch"""
    committer = InputGitAuthor(COMMITTER_NAME, COMMITTER_EMAIL)
    
    try:
        commit = repo.update_file(
            path=file_path,
            message=message,
            content=content,
            sha=sha,
            branch=branch,
            committer=committer
        )
        logger.info(f"File Updated on '{branch}' Branch.")
        return True
    except GithubException as e:
        logger.error(f"Failed to Update File on '{branch}' Branch: {e}")
        return False

def main():
    """Execute the Markdown Mimic Workflow"""
    try:
        # Initialize GitHub client and repository
        github_client = Github(token)
        repo = github_client.get_user().get_repo(repository)
        
        logger.info(f"Committer: {COMMITTER_NAME} <{COMMITTER_EMAIL}>")
        logger.info(f"Branch: {branch}")
        
        # Get file contents
        target_file = repo.get_contents(paste_file_location, ref=branch)
        target_content = decode_content(target_file.content)
        
        source_file = repo.get_contents(copy_file_location, ref=branch)
        source_content = decode_content(source_file.content)
        
        # Generate new content
        new_content = generate_new_content(source_content, target_content)
        
        # Only update if content has changed
        if new_content != target_content:
            success = update_file(
                repo=repo,
                file_path=target_file.path,
                content=new_content,
                message='🤖 - Updated with Markdown Mimic',
                sha=target_file.sha,
                branch=branch
            )
            
            if success:
                logger.info("Repository Updated Successfully")
            else:
                logger.error("Failed to Update Repository")
        else:
            logger.info("No Changes Detected. Skipping Update.")
            
    except KeyError as e:
        logger.error(f"Missing required environment variable: {e}.")
        if str(e) == "'INPUT_BRANCH'":
            logger.error("Branch must be specified using INPUT_BRANCH environment variable.")
    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    main()