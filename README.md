# Powertools Carbon

This repository is a collection of code examples using Powertools for AWS Lambda that can be generated as carbon.now.sh screenshot consistently using a configuration file and without using the website.

## Why this project exists

The core idea is to have a project folder for each language with examples that are correct and can be linted and verified using the specific dependencies and version. This allows to catch errors early in the IDE, write correct code and generate the images from your terminal, instead of copy pasting it to the website and configure it. 

It also enables a consistent visual output from the examples, so you don't have to care about all the settings if you'd use carbon.now.sh website from scratch. 

## How to use

1. Install the necessary dependencies by running `npm install` in your terminal.

2. To generate an image, use the `npm run carbon` script followed by the path to the file. For example, if you want to generate an image for a file located at `typescript/src/logger.ts`, you would use the following command:

```
npm run carbon ./typescript/src/logger.ts
```


## Limitations

**Network access.** Using carbon-cli project we send the code over the wire to the carbon.now.sh website and retrieve the rendered results. There is no option for now to run it locally

**Bulk mode.** It is only possible to generate a single file, this is a limitation of carbon-cli. You can't pass a folder, or a list of files to bulk generate many screenshots. 
