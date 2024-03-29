<h1 align="center">You Rock - A Personalized Contribution Appreciator.</h1>

[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

# What it does?

Sends out a personalized email appreciating the contribution with some **Badges** and **Image Processed Personalized Material**.

# Aim and Impact

This action will help :hash: **maintainers** to improve the `outreach` and Public Relations.

# What it looks like?

![](https://trello-attachments.s3.amazonaws.com/5f4c8eb8cd675c6f5dd4dc70/597x289/d295b59b0983b6853abffb00fc634440/YouRockEmail.gif)

# How to test?

<center><img src="Note.png" width="900"></img></center>

1. Just open a new issue on this [YouRock](https://github.com/TheShubham99/YouRock) Repo.
2. You'll receive a personalized email (email account linked to your **Github**)

![](./.github/YouRockDemo.gif)

# How to use it in your repo?

1. Clone the repository.
2. Copy the repository contents to your repository where you wish to add the **You Rock - Appreciator**.

## Setup Email Sending Account

1. Create a new gmail account for sending the emails.
2. Authorize Gmail to send automated emails via this tool https://myaccount.google.com/lesssecureapps

![](https://docs.bitnami.com/images/img/apps/common/google-security.png)

3. Create a [Github Secret](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) Called `GKEY` and add your gmail password to it.

4. Unlock the captcha link on sender account: https://accounts.google.com/DisplayUnlockCaptcha

## Setting up the action

1. Make sure your repository contains all the necessary files present in this repository.
2. Click on Actions and `create an action`.
   ![](https://docs.github.com/assets/images/help/repository/actions-tab.png)

3. Add code in `Appreciate.yml` to your workflow `yml` file.

## Customize your email contents

1. - Replace the `senders_email` in `Rock.py` with your newly created `email address` (on line 65)
   - Replace the `msg['From']` value with your email display name.

2. You can change the `glasses.png` with your Mask image. (make sure you rename it back to `glasses.png`)
3. You can change the `gold.png` with your Mask image. (make sure you rename it back to `gold.png`)

### Note:

- If you changed the file name of `glasses.png` and `gold.png` make sure to reflect in your `workflow`/`.yml`.

- The `glasses.png` will get placed on users face (in github avatar) and It will be sent only if there is a face in the users github avatar.

## How to change the contribution triggers?

you can edit the `Appreciate.yml` by changing the triggering conditions.

```
on:
  issues:
    types: opened
  pull_request:
    types: opened
    branches:
      - master
```

The default triggering conditions are -

1.  Issues - Opened
2.  Pull Request - Opened

You can change the job triggers according to your need.

[Learn More about the syntax for actions here.](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)

# Drop a ⭐ if you like it :)
