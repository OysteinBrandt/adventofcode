# TODO: web scraping challenge
# NOTE: Probably wize to check if SVG tool can draw as expected before we start scrape logic
#  - Add adventofcode.com authentication method so that we get correct data when scraping
#    - or use session? I.e.
#      _ga=<GA...>; _gid=<GA...>; session=<YOUR_SESSION_ID>
#  - Scrape HTML (using BeautifulSoup?)
#  - Extract data we need
#    * calendar drawing (combine uncompleted with completed)
#    * calendar day number
#    * stars
#  - Generate title
#  - Generate SVG file (with svgwrite? / drawSvg? / )

# NOTE: The README.md file for the given year should contain something like this:
#       <a href="https://adventofcode.com"><img src="2022/calendar.svg" width="80%" /></a>
#       Inspired by 🎄 Advent of Code (2015-2022) in C#

import urllib.request
response = urllib.request.urlopen("https://adventofcode.com").read()
print(response)

# $ py caledar_progress_gen.py
"""
b'<!DOCTYPE html>\n<html lang="en-us">\n<head>\n<meta charset="utf-8"/>\n<title>Advent of Code 2022</title>\n<!--[if lt IE 9]><script src="/static/html5.js"></script><![endif]-->\n<link href=\'//fonts.googleapis.com/css?family=Source+Code+Pro:300&subset=latin,latin-ext\' rel=\'stylesheet\' type=\'text/css\'/>\n<link rel="stylesheet" type="text/css" href="/static/style.css?30"/>\n<link rel="stylesheet alternate" type="text/css" href="/static/highcontrast.css?0" title="High Contrast"/>\n<link rel="shortcut icon" href="/favicon.png"/>\n<script>window.addEventListener(\'click\', function(e,s,r){if(e.target.nodeName===\'CODE\'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>\n</head><!--\n\n\n\n\nOh, hello!  Funny seeing you here.\n\nI appreciate your enthusiasm, but you aren\'t going to find much down here.\nThere certainly aren\'t clues to any of the puzzles.  The best surprises don\'t\neven appear in the source until you unlock them for real.\n\nPlease be careful with automated requests; I\'m not a massive company, and I can\nonly take so much traffic.  Please be considerate so that everyone gets to play.\n\nIf you\'re curious about how Advent of Code works, it\'s running on some custom\nPerl code. Other than a few integrations (auth, analytics, social media), I\nbuilt the whole thing myself, including the design, animations, prose, and all\nof the puzzles.\n\nThe puzzles are most of the work; preparing a new calendar and a new set of\npuzzles each year takes all of my free time for 4-5 months. A lot of effort\nwent into building this thing - I hope you\'re enjoying playing it as much as I\nenjoyed making it for you!\n\nIf you\'d like to hang out, I\'m @ericwastl on Twitter.\n\n- Eric Wastl\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-->\n<body>\n<header><div><h1 class="title-global"><a href="/">Advent of Code</a></h1><nav><ul><li><a href="/2022/about">[About]</a></li><li><a href="/2022/events">[Events]</a></li><li><a href="https://teespring.com/stores/advent-of-code" target="_blank">[Shop]</a></li><li><a href="/2022/auth/login">[Log In]</a></li></ul></nav></div><div><h1 class="title-event">&nbsp;<span class="title-event-wrap">{&apos;year&apos;:</span><a href="/2022">2022</a><span class="title-event-wrap">}</span></h1><nav><ul><li><a href="/2022">[Calendar]</a></li><li><a href="/2022/support">[AoC++]</a></li><li><a href="/2022/sponsors">[Sponsors]</a></li><li><a href="/2022/leaderboard">[Leaderboard]</a></li><li><a href="/2022/stats">[Stats]</a></li></ul></nav></div></header>\n\n<div id="sidebar">\n<div id="sponsor"><div class="quiet">Our <a href="/2022/sponsors">sponsors</a> help make Advent of Code possible:</div><div class="sponsor"><a href="https://www.rewe-digital.com/en" target="_blank" onclick="if(ga)ga(\'send\',\'event\',\'sponsor\',\'sidebar\',this.href);" rel="noopener">REWE digital</a> - Same same but different? Way more than that! Discover the new REWE digital and our Home of 2,200+ Riddle Solvers. Happy Coding, folks!</div></div>\n</div><!--/sidebar-->\n\n<main>\n<pre class="calendar calendar-beckon"><span aria-hidden="true" class="calendar-day25">@@@@@@@@@##@@##@@@@@@@#@@@@@@@#@###@@@@@@@###@@@@  <span class="calendar-day">25</span></span>\n<span aria-hidden="true" class="calendar-day24">@#@@@@@@@@#@@@#@#@@@@#@##@@#@@@@#@@@@#@#@@@@@@@@#  <span class="calendar-day">24</span></span>\n<span aria-hidden="true" class="calendar-day23">@@#@@@@#@@#@#@#@@@@@#@@@###@@#@@#@@@#@@@@@#@@@#@#  <span class="calendar-day">23</span></span>\n<span aria-hidden="true" class="calendar-day22">@#@@@@@@@#@@@@@@#@##@@#@@@@#@@#@##@#@@@@@@@#@@@#@  <span class="calendar-day">22</span></span>\n<span aria-hidden="true" class="calendar-day21">@@@####@@#@@@@#@@@@@@@#@#@@@@###@@@@@@@@#@@#@@@@#  <span class="calendar-day">21</span></span>\n<span aria-hidden="true" class="calendar-day20">@@@@@@@###@@@@@@#@@@@@@@@@##@@@@#@@@#@@##@@#@@@@@  <span class="calendar-day">20</span></span>\n<span aria-hidden="true" class="calendar-day19">#@@#@@#@@#@@@##@@#@|@@@@@|@#@@@#@@#@@#@@#@@#@@@@@  <span class="calendar-day">19</span></span>\n<span aria-hidden="true" class="calendar-day18">#@@@#@#@@@@#@@@@@#@@#@#@@@@#@|#@@#@@@@@@#@@#@@###  <span class="calendar-day">18</span></span>\n<span aria-hidden="true" class="calendar-day17">@@@##@#@#@#@#@@@@@@@#@#@@#@@@#@@#@@@#@@##@#@@#@@#  <span class="calendar-day">17</span></span>\n<span aria-hidden="true" class="calendar-day16">####@#@#@@#@@@@@@@@@@@@@#@@@@@#@@@#@@@@#@@@@#@@@@  <span class="calendar-day">16</span></span>\n<span aria-hidden="true" class="calendar-day15">@@####@@@@#@@#@@@@#@@##@@#@@@@#@@@@###@@@@@@@#@@@  <span class="calendar-day">15</span></span>\n<span aria-hidden="true" class="calendar-day14">@@@@#@@#@@@@#@@##@@#@@@@@@@@#@@@#@@##@@@@@@@@@@@@  <span class="calendar-day">14</span></span>\n<span aria-hidden="true" class="calendar-day13">@@#@@@@#@@@@#@@@###@@#@#####@###@@#@#@@@@@@@#@@@@  <span class="calendar-day">13</span></span>\n<span aria-hidden="true" class="calendar-day12">#@@@@@@#@@##@@##@@@#@@@@@@@@#@@#@|@@@@##|@@@#@#@@  <span class="calendar-day">12</span></span>\n<span aria-hidden="true" class="calendar-day11">@#@@@@#@@@@@@@@#@#@@#@@@@@##@@#@@@@@#@@##@#@@###@  <span class="calendar-day">11</span></span>\n<span aria-hidden="true" class="calendar-day10">@#@@@#@@@#@@@#@@@@@@@#@#@@@@@@@@#@@#@@@@#@@@@####  <span class="calendar-day">10</span></span>\n<span aria-hidden="true" class="calendar-day9">##@@@@@@@@@@#@@@@@@@@@#@#@@#@@@###@@@##@##@@##@@@  <span class="calendar-day"> 9</span></span>\n<span aria-hidden="true" class="calendar-day8">@@@#@#@#@@#@#@@@@@@@@#@#@@#@###@@#@##@@@@@#@@@@@@  <span class="calendar-day"> 8</span></span>\n<span aria-hidden="true" class="calendar-day7">@@#@@#@#@@@@#@@@@@#@@#@@@@@@@#@##@#@@@@@@#@@#@@@@  <span class="calendar-day"> 7</span></span>\n<span aria-hidden="true" class="calendar-day6">@@@@@@@@@#@@@#@@@@@@@#@#@@@#@##@@@@#@@@@@#@@@@#@@  <span class="calendar-day"> 6</span></span>\n<span aria-hidden="true" class="calendar-day5">@@@#@#@@@@#@@@@##@@@#@@##@#@@@@@#@@@#@@@@@@@@#@##  <span class="calendar-day"> 5</span></span>\n<span aria-hidden="true" class="calendar-day4">@@@@###@@@@#@@@@@@@@@@@##@@@@##@@@#@@@@@@@@@#@@@@  <span class="calendar-day"> 4</span><span id="calendar-countdown"></span><script>\n(function(){\nvar countdown = document.getElementById("calendar-countdown");\nif (!countdown) return;\nvar server_eta = 9609;\nvar key = "2022-4-"+server_eta;\nvar now = Math.floor(new Date().getTime()/1000);\nvar target = server_eta + now;\nif (sessionStorage) {\n  // if you navigate away and hit the back button, this makes sure the countdown doesn\'t start from the wrong time\n  var prev_target = sessionStorage.getItem("calendar-target");\n  try { prev_target = JSON.parse(prev_target); } catch(e){}\n  if (prev_target && typeof prev_target === \'object\' && prev_target.key === key) {\n    target = prev_target.target;\n  } else {\n    sessionStorage.setItem("calendar-target", JSON.stringify({key:key, target:target+1}));\n  }\n}\n\nvar interval = null;\nfunction update_countdown() {\n  var remaining = Math.ceil(target - new Date().getTime()/1000);\n  if (remaining <= 0) {\n    clearInterval(interval);\n    interval = null;\n    countdown.textContent = "";\n\n    var a = document.createElement("a");\n    a[String.fromCharCode(104,114,101,102)] = "/2022" + String.fromCharCode(47,100,97,121,47) + "4";\n    a.className = "calendar-day4 calendar-day-new";\n    var span = countdown.parentNode;\n    while (span.firstChild) {\n      a.appendChild(span.firstChild);\n    }\n    a.appendChild(document.createTextNode("   "));\n    span.parentNode.insertBefore(a, span);\n    span.parentNode.removeChild(span);\n    countdown.parentNode.removeChild(countdown);\n  } else {\n    var hours = Math.floor(remaining/60/60);\n    remaining -= hours * 60 * 60;\n    var minutes = Math.floor(remaining/60);\n    remaining -= minutes * 60;\n    var seconds = remaining;\n    countdown.textContent = (hours < 10 ? "0" : "") + hours + ":" + (minutes < 10 ? "0" : "") + minutes + ":" + (seconds < 10 ? "0" : "") + seconds;\n  }\n}\ninterval = setInterval(update_countdown,1000);\nupdate_countdown();\n})();\n</script></span>\n<a aria-label="Day 3" href="/2022/day/3" class="calendar-day3">#@@@@#@#@#@#@#@###@@@@@@@#@@@@##@@@#@@#@#@###@@@@  <span class="calendar-day"> 3</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>\n<a aria-label="Day 2" href="/2022/day/2" class="calendar-day2">@@@@#@@@@@#@@@#@#@@#@@#@##@@###@@@@@#@@##@@#@@@@@  <span class="calendar-day"> 2</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>\n<a aria-label="Day 1" href="/2022/day/1" class="calendar-day1">@@@@@@#@@#@#@@#@#@@@@#@@@@@@@@#@@@@@@@@@@@####@#@  <span class="calendar-day"> 1</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>\n</pre>\n</main>\n\n<!-- ga -->\n<script>\n(function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\nm=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n})(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\');\nga(\'create\', \'UA-69522494-1\', \'auto\');\nga(\'set\', \'anonymizeIp\', true);\nga(\'send\', \'pageview\');\n</script>\n<!-- /ga -->\n</body>\n</html>'
"""