<h1 align="center">You Rock - A Personalized Contribution Appreciator.</h1>

[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

# What it does?

Sends out a personalized email appreciating the contribution with some **Badges** and **Image Processed Personalized Material**.

# Aim and Impact

This action will help :hash: **maintainers** to improve the `outreach` and Public Relations.

# How to test?

Just open a new issue on this [YouRock](https://github.com/TheShubham99/YouRock) Repo.

![](./YouRockDemo.gif)

# How to use it in your repo?

1. Clone the repo.
2. Copy the repository contents to your repo where you wish to add the **Appreciator** (you can skip `.pdf`,`YouRockDemo.gif` and `me.jpg`)

# Setup Email Sending Account

1. Create a new gmail account for sending the emails.
2. Authorize Gmail to send automated emails via this tool https://myaccount.google.com/lesssecureapps
3. - Replace the `senders_email` in `Rock.py` with your newly created `email address` (on line 65)
   - Replace the `msg['From']=x` with your email display name.

4. Create a [Github Secret](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) Called `GKEY` and add your gmail password to it.

# Setting up the action

1. Make sure your repository contains all the necessary files present in this repository.
2. Click on Actions and create a action.
   ![](https://docs.github.com/assets/images/help/repository/actions-tab.png)

3. Add code in `Appreciate.yml` to your workflow `yml` file.

# How to chnage the contribution triggers?

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

# Drop a :star if you like it :)
