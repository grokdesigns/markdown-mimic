<h1 align="center">Markdown Mimic</h1>  

<p align="center">
	<a href="https://github.com/grokdesigns/markdown-mimic/stargazers"><img src="https://img.shields.io/github/stars/grokdesigns/markdown-mimic?colorA=363a4f&colorB=7dc4e4&style=for-the-badge"></a>
	<a href="https://github.com/grokdesigns/markdown-mimic/issues"><img src="https://img.shields.io/github/issues/grokdesigns/markdown-mimic?colorA=363a4f&colorB=7dc4e4&style=for-the-badge"></a>
	<a href="https://github.com/grokdesigns/markdown-mimic/contributors"><img src="https://img.shields.io/github/contributors/grokdesigns/markdown-mimic?colorA=363a4f&colorB=7dc4e4&style=for-the-badge"></a>
    <img src="https://img.shields.io/badge/language-python-blue?colorA=363a4f&colorB=7dc4e4&style=for-the-badge"/>
</p>

## Description

- This is a [GitHub Action](https://developer.github.com/actions/) to copy the content of a Markdown file and paste those contents within another Markdown file.

## Usage

1. Create a fine-grained access token [here](https://github.com/settings/personal-access-tokens).

2. Choose *Only select repositories* and select the repository in which this action will run.

3. This token will require read and write access on the *Contents* and *Commit statuses*"* options.

4. Save this token and create a new secret at: https://github.com\/\<username\>\/\<repository name\>\/settings\/secrets\/actions\/new. The name should be **MIMIC_TOKEN** and the secret should be your token (*should start with github_pat_*)

4. Create an .md file and enter the contents you would like copied. This file will be the *source*.

5. Choose your existing Markdown file (ex. README.md). This file will be the *mimic*. Choose where you would like content inserted and paste the following:

```js
<!--MIMIC_START-->
<!--MIMIC_END-->
```
Example Markdown:
```md
Paragraphs are separated by a blank line.

2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists
look like:

  * this one
  * that one

Latest News:
<!--MIMIC_START-->
<!--MIMIC_END-->

> Block quotes are
> written like so.

Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex., "it's all
in chapters 12--14").
```

In the above example, all content from your source file would be inserted under the "Latest News" section.

## Action

The following [workflow](https://docs.github.com/en/actions) will copy the data of the markdown file specified in the *SOURCE* environment variable. It will then insert that content into the file specified in TARGET.

```yml
name: Markdown Mimic - grokdesigns
on: 
  push:
    branches:
      - main                                             #Branch that will trigger action on new push.
  workflow_dispatch:
jobs:
  Markdown-Mimic:
    runs-on: ubuntu-latest                               #Platform that GitHub will use to run container.
    steps:
      - name: Mimic
        uses: docker://grokdesigns/markdown-mimic:latest #Docker image containing script.
        with:
          TOKEN: ${{ secrets.MIMIC_TOKEN }}              #Token you saved as a secret. Do not change.
          REPOSITORY : 'markdown-mimic'                  #Repository the action is running on.
          SOURCE : './assets/changingtextfile.md'        #File where you put changing content.
          TARGET : './README.md'                         #Target file that will have content inserted.
          BRANCH: 'main'                                 #Branch containing your files.
```

You can set this action up by navigating to your repo, clicking *Actions*, and then clicking *New workflow*. Alternately, you can download the [markdown-mimic.yml](markdown-mimic.yml) file and place it in your local repo at: /.github/workflows/ on your local repo and push to GitHub.

## Variables

The following input variables are all required for the action to run:

|Input variable|Description|
|--------------------|-----------|
|`TOKEN`|Your Github fine grained access token.|
|`REPOSITORY`|Name of repository where action is running (ex. `markdown-mimic-repo`).|
|`SOURCE`|Location of the markdown file from which you want to copy data (ex. `./file.md` or `./folder/file.md`.|
|`TARGET`|Location of the markdown file to which you want to paste the data (ex. `./README.md` or `./folder/file.md`).|
|`BRANCH`|Branch of your repository you want to run actions against (ex. `main` or `dev`).|

## Author

The Markdown Mimic GitHub action is written by [grokdesigns](https://github.com/grokdesigns).

## Credits

This action was inspired by [@ShreyamMaity](https://github.com/ShreyamMaity)'s [Copy-Paste-Action](https://github.com/ShreyamMaity/Copy-Paste-Action) project. Major changes include reducing the Docker image from 1.37GB to 59MB, leading to much faster action execution; support for including the email field in API calls to resolve authentication issues, addition of official github-actions[bot] as commiter.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.