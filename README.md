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
        uses: grokdesigns/markdown-mimic@v1.0.0
        with:
          branch_name: ${{ github.ref }}  #Don't change.
          commit_message: '🤖 - Generated via Markdown Mimic'
          file_ext: 'md'
          git_email: 'github-actions[bot]@users.noreply.github.com'
          git_username: 'github-actions[bot]'
          input_folder: 'templates'
          output_folder: 'output'
          skip_ci: 'yes' #BE VERY CAREFUL CHANGING THIS. IT COULD CREATE INFINITE WORKFLOWS.
```

2. Create markdown-mimic.yml in your repository under .github/workflows/ using the template.

In the files that you would like Markdown Mimic to insert content in, use the below code in the Markdown file:
```js
<!--MIMIC_START-->
<!--MIMIC_END-->
```

3. In the 'input_folder' you specify in your Workflow, create Markdown templates with `<filename>.mimic`, where `<filename>` matches the filename of your output file. I.e. if you create README.mimic as a template, it will be output as README.md (or other extension as you declare in the Workflow)


## Variables

The following input variables are all required for the action to run:

|Input variable|Description|
|--------------------|-----------|
|`branch_name`|Name of the branch the action is triggered by. This will be calculated automatically.|
|`commit_message`|Commit message that you would like attached to commits by the tool.|
|`file_ext`|File extension you wish to use for output files (generally .md).|
|`git_email`|Email address you want associated with commits by the tool.|
|`git_username`|Username you want associated with commits by the tool..|
|`input_folder`|Input folder where .mimic files will be stored in the repository.|
|`output_folder`|Output folder where .md (or specified extension) files will be stored in the repository.|
|`skip_ci`|Setting this to 'yes' will append [no ci] to commits by the tool so that it does not trigger itself.|

## Author

The Markdown Mimic GitHub action is written by [grokdesigns](https://github.com/grokdesigns).

## Credits

This action was inspired by [@ShreyamMaity](https://github.com/ShreyamMaity)'s [Copy-Paste-Action](https://github.com/ShreyamMaity/Copy-Paste-Action) project. It was completely rewritten to use the native abilities of GitHub Actions and remodeled to be used as an official Marketplace action.. This includes a new Docker image that we were able to reduce from 1.37GB to 131MB, so this action should run much faster.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.
