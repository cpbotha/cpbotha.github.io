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

I started using CloudFlare&#8217;s free tier on this blog, before Let&#8217;s Encrypt burst onto the scene, mostly for their [universal SSL][1]. However, as joepie91 [recently pointed out][2], this means that by design, CloudFlare has to decrypt all SSL traffic, and then re-encrypt it to send it to your original site with its self-signed or generic certificate (in my case). Apart from this, CloudFlare is a bit of overkill for this low-traffic site. 

<div class="figure">
  <p>
    <a href="https://letsencrypt.org/"><img src="https://letsencrypt.org/images/le-logo-standard.png" alt="le-logo-standard.png" /></a>
  </p></p>
</div>

Because I don&#8217;t need much of an excuse to try out something new, I used this as my excuse to try out [Let&#8217;s Encrypt][3], a fantastic new(ish) service which issues free 90 day certificates to anyone who can verify their domains. 

I was shocked with how easy this was on the webfaction shared (non root) hosting I&#8217;ve been using for years, and so I had to share. 

**WITNESS THE GREAT EASINESS:** 

<div id="outline-container-orgheadline1" class="outline-2">
  <h2 id="orgheadline1">
    Step 1: Install acme.sh
  </h2>
  
  <div class="outline-text-2" id="text-orgheadline1">
    <p>
      These two steps are to be performed whilst SSH&#8217;d in to your web host.
    </p>
    
    <p>
      First we install <a href="https://github.com/Neilpang/acme.sh">the wonderful acme.sh</a> by following the one-liner on its website:
    </p>
    
    <div class="org-src-container">
      <pre class="src src-sh">curl https://get.acme.sh | sh
</pre>
    </div>
    
    <p>
      At this junction, as they say, it&#8217;s best to log out and in again, so that the acme.sh alias and environment variable can be setup.
    </p>
  </div>
</div>

<div id="outline-container-orgheadline2" class="outline-2">
  <h2 id="orgheadline2">
    Step 2: Issue shiny new SSL certificate
  </h2>
  
  <div class="outline-text-2" id="text-orgheadline2">
    <p>
      We then get <code>acme.sh</code> to verify the website using the webroot method, and to request a certificate for the two domains <code>cpbotha.net</code> and <code>www.cbbotha.net</code>:
    </p>
    
    <div class="org-src-container">
      <pre class="src src-sh">acme.sh --issue -d cpbotha.net -d www.cpbotha.net -w ~/webapps/wp
</pre>
    </div>
    
    <p>
      The argument following <code>-w</code> is the directory exposed by the website <code>http://cpbotha.net/</code>. Note that this is still <code>http</code>; Let&#8217;s Encrypt queries a special file left there by acme.sh to confirm that you actually manage the specified domain.
    </p>
    
    <p>
      After a few seconds of progress output, I was left with a shiny certificate (as well as the CSR, key, and so forth) in <code>~/.acme.sh/cpbotha.net/</code>
    </p>
  </div>
</div>

<div id="outline-container-orgheadline3" class="outline-2">
  <h2 id="orgheadline3">
    Step 3: Install shiny new SSL certificate
  </h2>
  
  <div class="outline-text-2" id="text-orgheadline3">
    <p>
      On Webfaction, one has to file a support ticket for this. My request was formulated thusly, and was correctly acted upon in about 5 minutes:
    </p>
    
    <blockquote>
      <p>
        Could you please install the following SSL certificate for the website cpbotha_SSL &#8211; reachable at <a href="https://cpbotha.net/">https://cpbotha.net/</a>:
      </p>
      
      <ul class="org-ul">
        <li>
          cert is in <code>/home/cpbotha/.acme.sh/cpbotha.net/cpbotha.net.cer</code>
        </li>
        <li>
          key is in <code>/home/cpbotha/.acme.sh/cpbotha.net/cpbotha.net.key</code>
        </li>
        <li>
          intermediate CA cert is in <code>/home/cpbotha/.acme.sh/cpbotha.net/ca.cer</code>
        </li>
        <li>
          full chain certs is there: <code>/home/cpbotha/.acme.sh/cpbotha.net/fullchain.cer</code>
        </li>
      </ul>
      
      <p>
        Thanks!
      </p>
    </blockquote>
  </div>
  
  <div id="outline-container-orgheadline4" class="outline-3">
    <h3 id="orgheadline4">
      Update on 2016-10-25
    </h3>
    
    <div class="outline-text-3" id="text-orgheadline4">
      <p>
        It is now possible to install the new certs all by yourself using the webfaction panel or the API! Read the <a href="https://blog.webfaction.com/2016/09/manage-ssl-certificates-with-the-control-panel/">announcement blog post</a> for more information.
      </p>
    </div>
  </div>
</div>

<div id="outline-container-orgheadline5" class="outline-2">
  <h2 id="orgheadline5">
    Bonus level: In 90 &#8211; k days, simply re-run acme.sh
  </h2>
  
  <div class="outline-text-2" id="text-orgheadline5">
    <p>
      At any point, you can request certificates for any other domains that you may be hosting on your webfaction.
    </p>
    
    <p>
      At regular intervals, or in slightly fewer than 90 days, simply run:
    </p>
    
    <div class="org-src-container">
      <pre class="src src-sh">acme.sh --renewAll
</pre>
    </div>
    
    <p>
      To have acme.sh renew any of your certificates that are up for renewal. Just remember to create a new support ticket to have the renewed certificates installed for the relevant domains.
    </p>
  </div>
  
  <div id="outline-container-orgheadline6" class="outline-3">
    <h3 id="orgheadline6">
      acme.sh cronjob
    </h3>
    
    <div class="outline-text-3" id="text-orgheadline6">
      <p>
        Unbeknownst to be (I should have read the docs) acme.sh had cleverly installed a user cronjob to check for renewals. When I attempted to renew two of my certs, I saw that it had already done so automatically, so I only had to install the updated versions.
      </p>
    </div>
  </div>
</div>

<div id="outline-container-orgheadline7" class="outline-2">
  <h2 id="orgheadline7">
    Boss level: htaccess-based redirect from HTTP to HTTPS
  </h2>
  
  <div class="outline-text-2" id="text-orgheadline7">
    <p>
      Now that I have my SSL setup, I would prefer for users who go to the HTTP site to be 301 forwarded to the HTTPS version. On Webfaction, I can do that with the following addition to the site <code>.htaccess</code> file:
    </p>
    
    <div class="org-src-container">
      <pre class="src src-html">&lt;<span style="color: #93E0E3;">IfModule</span> mod_rewrite.c&gt;
RewriteEngine On
# we're behind nginx ssl proxy, hence the non-standard check for no-SSL:
RewriteCond %{HTTP:X-Forwarded-SSL} !on
RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
&lt;/<span style="color: #93E0E3;">IfModule</span>&gt;
</pre>
    </div>
    
    <p>
      <b>Important:</b> webfaction is using nginx as their SSL frontend, so we check for the X-Forwarded-SSL header.
    </p>
  </div>
</div>

 [1]: https://blog.cloudflare.com/introducing-universal-ssl/
 [2]: http://cryto.net/~joepie91/blog/2016/07/14/cloudflare-we-have-a-problem/
 [3]: https://letsencrypt.org/
