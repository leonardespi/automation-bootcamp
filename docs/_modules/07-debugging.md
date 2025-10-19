---
layout: module
title: "07 Debugging"
permalink: /modules/07-debugging/
---

<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>07 Debugging</title>
<style>
:root{
  --bg:#fff;
  --fg:#111;
  --muted:#555;
  --border:#ddd;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--bg);color:var(--fg);font:16px/1.6 ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace}
.container{max-width:72ch;margin:0 auto;padding:2rem 1rem}
header{margin-bottom:1rem;border-bottom:1px solid var(--border);padding-bottom:0.75rem}
h1,h2,h3,h4,h5,h6{line-height:1.25;margin:1.2em 0 0.6em}
p{margin:0.6em 0}
a{color:inherit;text-decoration:underline}
nav ul{list-style:none;padding:0;margin:0.25rem 0;display:flex;flex-wrap:wrap;gap:0.5rem}
nav a{padding:0.25rem 0.5rem;border:1px solid var(--border);border-radius:0.5rem;text-decoration:none}
footer{margin-top:2rem;color:var(--muted);font-size:0.9em}
pre.code{background:#f6f6f6;border:1px solid var(--border);padding:1rem;overflow:auto;border-radius:0.5rem}
code{background:#f0f0f0;padding:0.1rem 0.25rem;border-radius:0.25rem}
blockquote{border-left:3px solid var(--border);margin:1rem 0;padding:0.1rem 0 0.1rem 1rem;color:var(--muted)}
hr{border:none;border-top:1px solid var(--border);margin:2rem 0}
ul,ol{padding-left:1.25rem}
.header-title{font-weight:700}
.breadcrumb{color:var(--muted);font-size:0.9em}
</style>
<body>
  <div class="container">
    <header>
      <div class="header-title">07 Debugging</div>
      <nav><ul><li><a href="index.html">Index</a></li><li><a href="01-introduction.html">01 Introduction</a></li><li><a href="02-python-basics.html">02 Python Basics</a></li><li><a href="03-web-automation.html">03 Web Automation</a></li><li><a href="04-pom-architecture.html">04 Pom Architecture</a></li><li><a href="05-assertions-reporting.html">05 Assertions Reporting</a></li><li><a href="06-ci-integration.html">06 Ci Integration</a></li><li><a href="07-debugging.html">07 Debugging</a></li><li><a href="08-capstone-project.html">08 Capstone Project</a></li></ul></nav>
    </header>
    <main>
      <p>&lt;style&gt; body { text-align: justify; } &lt;/style&gt;</p>
<h1>Module 7 — Debugging &amp; Deflaking</h1>

<p><strong>Symptoms of flakiness:</strong> timeouts, stale elements, order dependence. <strong>Tactics:</strong> explicit waits, stable locators, test isolation, retries (sparingly).</p>

<p><strong>Task:</strong> deliberately break a wait, inspect failure logs, fix with <code>WebDriverWait</code>.</p>

    </main>
    <footer>
      Generated on 2025-10-19 20:55
    </footer>
  </div>
</body>
</html>
