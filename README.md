<h1 align="center">Markdown Mimic</h1>  

<p align="center">
	<a href="https://github.com/grokdesigns/markdown-mimic/stargazers"><img src="https://img.shields.io/github/stars/grokdesigns/markdown-mimic?colorA=363a4f&colorB=7dc4e4&style=for-the-badge"></a>
	<a href="https://github.com/grokdesigns/markdown-mimic/issues"><img src="https://img.shields.io/github/issues/grokdesigns/markdown-mimic?colorA=363a4f&colorB=7dc4e4&style=for-the-badge"></a>
	<a href="https://github.com/grokdesigns/markdown-mimic/contributors"><img src="https://img.shields.io/github/contributors/grokdesigns/markdown-mimic?colorA=363a4f&colorB=7dc4e4&style=for-the-badge"></a>
    <img src="https://img.shields.io/badge/language-python-blue?colorA=363a4f&colorB=7dc4e4&style=for-the-badge"/>
</p>

## Description

- This is a [GitHub Action](https://developer.github.com/actions/) to copy the content of a one text file and paste those contents within another text file.

## Usage

1. Download the [example_workflow.yml](example_workflow.yml)

```yml
name: Markdown Mimic Workflow
on:
  push:
    branches:
      - main
jobs:
  Markdown-Mimic-Action:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Markdown Mimic
        uses: grokdesigns/markdown-mimic@1.1.0 #Should match latest release.
        with:
          git_username: 'github-actions[bot]' #Username that will be attributed to the commit.
          git_email: 'github-actions[bot]@users.noreply.github.com' #Email that will be attributed to the commit.
          skip_ci: 'yes' #BE VERY CAREFUL CHANGING THIS. IT COULD CREATE INFINITE WORKFLOWS.
          commit_message: '🤖 - Generated via Markdown Mimic' #Message that will be attributed to the commit.
          file_exts: 'md,txt' #File extension(s) that you would like Markdown Mimic to search through for placeholders.
          overwrite_original: 1 #Overwrite original files. If set to 0, updated files will be placed in output_folder in same folder structure..
          output_folder: 'outputs' #Only used if overwrite_original: 0
          input_folder: 'templates' #Location of *.mimic templates.
          branch_name: ${{ github.ref }}  #Don't change, will automatically be assigned from branch at top of workflow.

```

2. Create markdown-mimic.yml in your repository under .github/workflows/ using the template.

3. In the templates directory, create your Markdown or plaintext templates. Name them based on the placeholder you would like its contents to replace.

## Examples
   
|Template Filename|Outcome|
|--------------------|-----------|
|`readme.mimic`|All files with the file extensions specified in options, with the `<!--MIMIC_README_START--> and <!--MIMIC_README_END-->)` placeholder in them, will have the contents replaced with the contents of readme.mimic|
|`legalese.mimic`|All files with the file extensions specified in options, with the `<!--MIMIC_LEGALESE_START--> and <!--MIMIC_LEGALESE_END-->)` placeholder in them, will have the contents replaced with the contents of legalese.mimic|
|`boilerplate.mimic`|All files with the file extensions specified in options, with the `<!--MIMIC_BOILERPLATE_START--> and <!--MIMIC_BOILERPLATEE_END-->)` placeholder in them, will have the contents replaced with the contents of boilerplate.mimic|
|`grey-fox.mimic`|All files with the file extensions specified in options, with the `<!--MIMIC_GREY-FOX_START--> and <!--MIMIC_GREY-FOX_END-->)` placeholder in them, will have the contents replaced with the contents of grey-fox.mimic|
|`project-x.mimic`|All files with the file extensions specified in options, with the `<!--MIMIC_PROJECT-X_START--> and <!--MIMIC_PROJECT-X_END-->)` placeholder in them, will have the contents replaced with the contents of project-x.mimic|

## Variables

The following input variables are all required for the action to run:

|Input variable|Description|
|--------------------|-----------|
|`branch_name`|Name of the branch the action is triggered by. This will be calculated automatically.|
|`commit_message`|Commit message that you would like attached to commits by the tool.|
|`file_ext`|File extension(s) you wish to search for placeholders.|
|`git_email`|Email address you want associated with commits by the tool.|
|`git_username`|Username you want associated with commits by the tool.|
|`input_folder`|Input folder where .mimic files will be stored in the repository.|
|`output_folder`|Output folder where .md (or specified extension) files will be stored in the repository if not overwriting originals.|
|`overwrite_original`|Overwrite original files in place or output to outputs folder (a new branch will be created either way).|
|`skip_ci`|Setting this to 'yes' will append [no ci] to commits by the tool so that it does not trigger itself.|

## Performance

50k files, 5250 files with Markdown Mimic placeholders, 9 second execution.
![image](https://github.com/user-attachments/assets/09c939f2-9ff0-4221-b83f-66e44bde7ec3)

![image](https://github.com/user-attachments/assets/f0d4c67c-e46f-4083-83e0-4934cce41b67)


## Author

The Markdown Mimic GitHub action is written by [grokdesigns](https://github.com/grokdesigns).

## Credits

This action was inspired by [@ShreyamMaity](https://github.com/ShreyamMaity)'s [Copy-Paste-Action](https://github.com/ShreyamMaity/Copy-Paste-Action) project. It was completely rewritten to use the native abilities of GitHub Actions and remodeled to be used as an official Marketplace action.. This includes a new Docker image that we were able to reduce from 1.37GB to 131MB, so this action should run much faster.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.
