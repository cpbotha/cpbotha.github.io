---
title: Installing free Let’s Encrypt SSL certificates on webfaction in 3 easy steps
author: cpbotha
type: post
date: 2016-07-18T19:31:00+00:00
url: /2016/07/18/installing-free-lets-encrypt-ssl-certificates-on-webfaction-in-3-easy-steps/
categories:
  - howto
tags:
  - 301
  - cloudflare
  - encryption
  - htaccess
  - nerdery
  - redirect
  - ssl
  - webfaction

---

**WARNING on 2020-02-24: webfaction has been bought by godaddy and will soon
close down. [I have recently moved
out](/2020/02/23/weekly-head-voices-189-all-systems-green/#the-whole-cpbothanet-hive-has-been-migrated-to-a-small-hetzner-server)
and am now keeping all of my Let's Encrypt certificates up to date with the
official [certbot tool](https://certbot.eff.org/).**

**WARNING: High levels of NERD ahead.** 

I started using CloudFlare’s free tier on this blog, before Let’s Encrypt burst onto the scene, mostly for their [universal SSL][1]. However, as joepie91 [recently pointed out][2], this means that by design, CloudFlare has to decrypt all SSL traffic, and then re-encrypt it to send it to your original site with its self-signed or generic certificate (in my case). Apart from this, CloudFlare is a bit of overkill for this low-traffic site. 

<div class="figure">
<p>
<a href="https://letsencrypt.org/"><img alt="le-logo-standard.png" src="https://letsencrypt.org/images/le-logo-standard.png"/></a>
</p>
</div>

Because I don’t need much of an excuse to try out something new, I used this as my excuse to try out [Let’s Encrypt][3], a fantastic new(ish) service which issues free 90 day certificates to anyone who can verify their domains. 

I was shocked with how easy this was on the webfaction shared (non root) hosting I’ve been using for years, and so I had to share. 

**WITNESS THE GREAT EASINESS:** 

## Step 1: Install acme.sh

These two steps are to be performed whilst SSH’d in to your web host.

First we install <a href="https://github.com/Neilpang/acme.sh">the wonderful acme.sh</a> by following the one-liner on its website:

'''shell
curl https://get.acme.sh | sh
'''

At this junction, as they say, it’s best to log out and in again, so that the acme.sh alias and environment variable can be setup.

## Step 2: Issue shiny new SSL certificate

We then get <code>acme.sh</code> to verify the website using the webroot method, and to request a certificate for the two domains <code>cpbotha.net</code> and <code>www.cbbotha.net</code>:

```shell
acme.sh --issue -d cpbotha.net -d www.cpbotha.net -w ~/webapps/wp
```

The argument following <code>-w</code> is the directory exposed by the website <code>http://cpbotha.net/</code>. Note that this is still <code>http</code>; Let’s Encrypt queries a special file left there by acme.sh to confirm that you actually manage the specified domain.

After a few seconds of progress output, I was left with a shiny certificate (as well as the CSR, key, and so forth) in <code>~/.acme.sh/cpbotha.net/</code>

## Step 3: Install shiny new SSL certificate

On Webfaction, one has to file a support ticket for this. My request was formulated thusly, and was correctly acted upon in about 5 minutes:


> Could you please install the following SSL certificate for the website cpbotha_SSL – reachable at <a href="https://cpbotha.net/">https://cpbotha.net/</a>:
>
> - cert is in <code>/home/cpbotha/.acme.sh/cpbotha.net/cpbotha.net.cer</code>
> - key is in <code>/home/cpbotha/.acme.sh/cpbotha.net/cpbotha.net.key</code>
> - intermediate CA cert is in <code>/home/cpbotha/.acme.sh/cpbotha.net/ca.cer</code>
> - full chain certs is there: <code>/home/cpbotha/.acme.sh/cpbotha.net/fullchain.cer</code>
> 
> Thanks!
  

### Update on 2016-10-25

It is now possible to install the new certs all by yourself using the webfaction panel or the API! Read the <a href="https://blog.webfaction.com/2016/09/manage-ssl-certificates-with-the-control-panel/">announcement blog post</a> for more information.

## Bonus level: In 90 – k days, simply re-run acme.sh

At any point, you can request certificates for any other domains that you may be hosting on your webfaction.

At regular intervals, or in slightly fewer than 90 days, simply run:

```shell
acme.sh --renewAll
```

To have acme.sh renew any of your certificates that are up for renewal. Just remember to create a new support ticket to have the renewed certificates installed for the relevant domains.

### acme.sh cronjob


Unbeknownst to be (I should have read the docs) acme.sh had cleverly installed a user cronjob to check for renewals. When I attempted to renew two of my certs, I saw that it had already done so automatically, so I only had to install the updated versions.

## Boss level: htaccess-based redirect from HTTP to HTTPS

Now that I have my SSL setup, I would prefer for users who go to the HTTP site to be 301 forwarded to the HTTPS version. On Webfaction, I can do that with the following addition to the site <code>.htaccess</code> file:

<div class="org-src-container">
<pre class="src src-html">&lt;<span style="color: #93E0E3;">IfModule</span> mod_rewrite.c&gt;
RewriteEngine On
# we're behind nginx ssl proxy, hence the non-standard check for no-SSL:
RewriteCond %{HTTP:X-Forwarded-SSL} !on
RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
&lt;/<span style="color: #93E0E3;">IfModule</span>&gt;
</pre>
</div>
<b>Important:</b> webfaction is using nginx as their SSL frontend, so we check for the X-Forwarded-SSL header.

 [1]: https://blog.cloudflare.com/introducing-universal-ssl/
 [2]: http://cryto.net/~joepie91/blog/2016/07/14/cloudflare-we-have-a-problem/
 [3]: https://letsencrypt.org/
