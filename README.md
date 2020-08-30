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
3. Replace the `senders_email` in `Rock.py` on line 65.
4. Create a github Secret Called `GKEY` and add your gmail password to it.
5. Add code in actions.yml to your workflow yml.
