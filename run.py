from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Joever L. Sayson | Computer Engineer Portfolio</title>
<meta name="description" content="Portfolio of Joever L. Sayson — Computer Engineering Graduate, researcher, AI/ML and computer vision developer.">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

:root{
  --bg:#070b12; --bg2:#0c1220; --card:rgba(16,24,39,.72);
  --text:#eef4ff; --muted:#9aa9bd; --line:rgba(148,163,184,.15);
  --accent:#61dafb; --accent2:#8b5cf6; --good:#4ade80;
  --shadow:0 25px 80px rgba(0,0,0,.35);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  font-family:Inter,system-ui,sans-serif;color:var(--text);background:
  radial-gradient(circle at 15% 10%,rgba(97,218,251,.13),transparent 28%),
  radial-gradient(circle at 85% 25%,rgba(139,92,246,.14),transparent 30%),
  var(--bg);
  overflow-x:hidden;
}
body:before{
  content:"";position:fixed;inset:0;pointer-events:none;opacity:.14;
  background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);
  background-size:55px 55px;mask-image:linear-gradient(to bottom,#000,transparent 85%);
}
a{color:inherit;text-decoration:none}
.container{width:min(1120px,92%);margin:auto}
nav{
  position:fixed;top:0;left:0;width:100%;z-index:50;
  background:rgba(7,11,18,.68);backdrop-filter:blur(16px);
  border-bottom:1px solid var(--line)
}
.nav-inner{height:72px;display:flex;align-items:center;justify-content:space-between}
.logo{font-family:"Space Grotesk";font-size:1.25rem;font-weight:700}
.logo span{color:var(--accent)}
.nav-links{display:flex;gap:25px;color:var(--muted);font-size:.9rem}
.nav-links a{transition:.25s}.nav-links a:hover{color:var(--accent)}
.menu{display:none;background:none;border:0;color:white;font-size:1.5rem}

.hero{min-height:100vh;display:grid;place-items:center;padding:120px 0 70px;position:relative}
.hero-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:70px;align-items:center}
.badge{
  display:inline-flex;align-items:center;gap:8px;padding:8px 13px;border:1px solid var(--line);
  background:rgba(255,255,255,.035);border-radius:999px;color:#c9d5e6;font-size:.82rem;margin-bottom:22px
}
.dot{width:8px;height:8px;border-radius:50%;background:var(--good);box-shadow:0 0 15px var(--good);animation:pulse 1.7s infinite}
@keyframes pulse{50%{transform:scale(1.5);opacity:.5}}
h1{font-family:"Space Grotesk";font-size:clamp(3rem,7vw,6.5rem);line-height:.92;letter-spacing:-.065em}
.gradient{background:linear-gradient(100deg,var(--accent),#fff 43%,#a78bfa);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero p{color:var(--muted);font-size:1.08rem;line-height:1.8;max-width:680px;margin:25px 0}
.buttons{display:flex;gap:13px;flex-wrap:wrap}
.btn{padding:13px 19px;border-radius:12px;border:1px solid var(--line);font-weight:600;font-size:.9rem;transition:.25s}
.btn.primary{background:linear-gradient(135deg,var(--accent),#3b82f6);color:#061018;border:0}
.btn:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(97,218,251,.12)}
.hero-card{
  min-height:440px;border:1px solid var(--line);background:linear-gradient(145deg,rgba(18,30,49,.88),rgba(9,14,25,.7));
  border-radius:30px;box-shadow:var(--shadow);position:relative;overflow:hidden;display:grid;place-items:center
}
.orbit{width:250px;height:250px;border:1px solid rgba(97,218,251,.3);border-radius:50%;position:relative;animation:spin 16s linear infinite}
.orbit:before,.orbit:after{content:"";position:absolute;border:1px solid rgba(139,92,246,.3);border-radius:50%;inset:30px;transform:rotate(60deg)}
.orbit:after{inset:65px;transform:rotate(-45deg)}
.core{
  position:absolute;inset:75px;border-radius:50%;display:grid;place-items:center;
  background:radial-gradient(circle,#1e293b,#0b1220);border:1px solid rgba(97,218,251,.5);
  box-shadow:0 0 60px rgba(97,218,251,.18)
}
.core span{font-family:"Space Grotesk";font-weight:700;font-size:2.8rem}
.node{position:absolute;width:13px;height:13px;background:var(--accent);border-radius:50%;box-shadow:0 0 22px var(--accent)}
.n1{top:15px;left:50%}.n2{right:20px;bottom:55px;background:#a78bfa}.n3{left:20px;bottom:55px;background:#4ade80}
@keyframes spin{to{transform:rotate(360deg)}}
.floating{position:absolute;padding:9px 12px;background:rgba(8,13,23,.9);border:1px solid var(--line);border-radius:10px;font-size:.72rem;color:#b9c8dc;animation:float 4s ease-in-out infinite}
.f1{top:50px;right:30px}.f2{bottom:55px;left:25px;animation-delay:1s}.f3{top:46%;right:20px;animation-delay:2s}
@keyframes float{50%{transform:translateY(-10px)}}

section{padding:100px 0}
.section-head{margin-bottom:42px}.eyebrow{color:var(--accent);font-size:.78rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase}
h2{font-family:"Space Grotesk";font-size:clamp(2rem,4vw,3.4rem);margin-top:8px;letter-spacing:-.04em}
.section-head p{color:var(--muted);max-width:650px;line-height:1.7;margin-top:12px}
.grid{display:grid;gap:18px}
.about-grid{grid-template-columns:1fr 1fr}
.card{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:25px;backdrop-filter:blur(12px);transition:.3s}
.card:hover{transform:translateY(-5px);border-color:rgba(97,218,251,.28)}
.card h3{font-family:"Space Grotesk";margin-bottom:12px}
.card p{color:var(--muted);line-height:1.75}
.skills{grid-template-columns:repeat(4,1fr)}
.skill{min-height:150px;transition:.35s}
.skill .icon{
  width:46px;height:46px;margin-bottom:15px;display:flex;align-items:center;justify-content:center;
  border-radius:13px;background:linear-gradient(145deg,rgba(97,218,251,.14),rgba(139,92,246,.14));
  border:1px solid rgba(148,163,184,.18);color:var(--accent);transition:.4s
}
.skill .icon svg{width:23px;height:23px}
.skill:hover{transform:translateY(-6px) scale(1.02);border-color:rgba(97,218,251,.35)}
.skill:hover .icon{transform:rotate(-8deg) scale(1.12);color:#fff;box-shadow:0 10px 26px rgba(97,218,251,.25)}
.skill small{color:var(--muted)}
.langs{grid-template-columns:repeat(6,1fr);gap:14px}
.lang{min-height:120px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:9px;padding:18px 10px;transition:.35s}
.lang-badge{
  width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;
  font-family:"Space Grotesk";font-weight:700;font-size:.92rem;letter-spacing:-.02em;
  box-shadow:0 10px 24px rgba(0,0,0,.35);transition:.4s
}
.lang:hover{transform:translateY(-6px);border-color:rgba(139,92,246,.4);box-shadow:0 14px 30px rgba(139,92,246,.15)}
.lang:hover .lang-badge{transform:translateY(-4px) rotate(-6deg) scale(1.08)}
.lang small{color:var(--muted);font-size:.72rem}
.php-badge{background:linear-gradient(135deg,#8993c4,#6a7bc2);color:#fff}
.py-badge{background:linear-gradient(135deg,#ffd43b 0 50%,#3776ab 50%);color:#0b1220}
.js-badge{background:#f7df1e;color:#1a1a1a}
.cs-badge{background:linear-gradient(135deg,#9b4f96,#68217a);color:#fff}
.c-badge{background:linear-gradient(135deg,#4f80c4,#2b5a94);color:#fff}
.cpp-badge{background:linear-gradient(135deg,#0081c2,#004a80);color:#fff}
@media(max-width:850px){.langs{grid-template-columns:repeat(3,1fr)}}
@media(max-width:520px){.langs{grid-template-columns:repeat(2,1fr)}}
.projects{grid-template-columns:repeat(2,1fr)}
.project{position:relative;overflow:hidden;min-height:260px}
.project:after{content:"";position:absolute;width:160px;height:160px;right:-50px;top:-50px;border-radius:50%;background:rgba(97,218,251,.08);filter:blur(4px)}
.tag{display:inline-block;padding:5px 9px;border-radius:999px;background:rgba(97,218,251,.09);color:var(--accent);font-size:.7rem;margin:4px 4px 0 0}
.project p{margin:10px 0 18px}
.research{border-left:2px solid var(--accent);border-radius:0 18px 18px 0}
.timeline{position:relative;display:grid;gap:18px}
.timeline:before{content:"";position:absolute;left:9px;top:10px;bottom:10px;width:1px;background:var(--line)}
.time-item{padding-left:35px;position:relative}.time-item:before{content:"";position:absolute;left:4px;top:8px;width:11px;height:11px;border-radius:50%;background:var(--accent);box-shadow:0 0 15px var(--accent)}
.date{color:var(--accent);font-size:.76rem;font-weight:700;letter-spacing:.08em}
.contact{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.contact .card{min-height:180px}
footer{padding:35px 0;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem}
.ai{
  position:fixed;right:24px;bottom:24px;z-index:60;width:58px;height:58px;border:0;border-radius:50%;
  background:linear-gradient(135deg,var(--accent),#8b5cf6);cursor:pointer;box-shadow:0 12px 40px rgba(97,218,251,.25);font-size:1.3rem
}
.ai-panel{
  position:fixed;right:24px;bottom:94px;width:min(360px,calc(100vw - 32px));z-index:60;
  background:#0b1220;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow);
  padding:18px;display:none
}
.ai-panel.show{display:block;animation:pop .25s ease}
@keyframes pop{from{opacity:0;transform:translateY(10px) scale(.98)}}
.ai-panel h3{font-family:"Space Grotesk";margin-bottom:6px}.ai-panel p{font-size:.82rem;color:var(--muted);line-height:1.6}
.ai-answer{margin-top:12px;padding:12px;border-radius:12px;background:rgba(255,255,255,.04);font-size:.82rem;line-height:1.6;min-height:45px}
.ai-input{display:flex;gap:7px;margin-top:10px}.ai-input input{min-width:0;flex:1;background:#111a2b;border:1px solid var(--line);color:white;padding:10px;border-radius:10px;outline:none}
.ai-input button{border:0;border-radius:10px;padding:0 13px;background:var(--accent);cursor:pointer}
.reveal{opacity:0;transform:translateY(25px);transition:.7s}.reveal.visible{opacity:1;transform:none}
@media(max-width:850px){
 .hero-grid,.about-grid,.contact,.projects{grid-template-columns:1fr}
 .skills{grid-template-columns:repeat(2,1fr)}
 .nav-links{display:none}.menu{display:block}
 .hero-card{min-height:350px}
}
@media(max-width:520px){.skills{grid-template-columns:1fr}section{padding:75px 0}.nav-inner{height:64px}}
</style>
</head>
<body>

<nav>
  <div class="container nav-inner">
    <a class="logo" href="#home">JLS<span>.</span></a>
    <div class="nav-links">
      <a href="#about">About</a><a href="#skills">Skills</a><a href="#languages">Languages</a><a href="#projects">Projects</a>
      <a href="#research">Research</a><a href="#experience">Experience</a><a href="#contact">Contact</a>
    </div>
    <button class="menu" onclick="document.querySelector('.nav-links').classList.toggle('mobile')">☰</button>
  </div>
</nav>

<main id="home">
<section class="hero">
  <div class="container hero-grid">
    <div class="reveal">
      <div class="badge"><span class="dot"></span> Computer Engineering Graduate · AI / ML / Systems</div>
      <h1>Building <span class="gradient">intelligent</span><br>technology.</h1>
      <p>
        I'm <strong>Joever L. Sayson</strong>, a Computer Engineering graduate and technology builder
        focused on Artificial Intelligence, Machine Learning, Computer Vision, hardware,
        system configuration, and practical automation.
      </p>
      <div class="buttons">
        <a class="btn primary" href="#projects">Explore My Work</a>
        <a class="btn" href="#research">View Research</a>
      </div>
    </div>
    <div class="hero-card reveal">
      <div class="orbit"><div class="core"><span>AI</span></div><i class="node n1"></i><i class="node n2"></i><i class="node n3"></i></div>
      <div class="floating f1">YOLOv3 · CNN</div>
      <div class="floating f2">Transformers · Keras</div>
      <div class="floating f3">Hardware + Systems</div>
    </div>
  </div>
</section>

<section id="about">
<div class="container">
  <div class="section-head reveal"><div class="eyebrow">01 · About</div><h2>Engineer with a builder mindset.</h2>
  <p>Combining software intelligence with hardware and system-level problem solving.</p></div>
  <div class="grid about-grid">
    <div class="card reveal"><h3>Who I am</h3><p>
      Computer Engineering graduate with hands-on experience developing AI and Computer Vision projects,
      configuring computer systems, troubleshooting hardware/software, and integrating intelligent
      technologies with real-world applications.
    </p></div>
    <div class="card reveal"><h3>What I work with</h3><p>
      My technical interests include machine learning, image classification, object detection,
      computer vision, embedded systems, system configuration, networking fundamentals, and
      software-hardware integration.
    </p></div>
  </div>
</div>
</section>

<section id="skills">
<div class="container">
  <div class="section-head reveal"><div class="eyebrow">02 · Expertise</div><h2>Technical toolkit.</h2></div>
  <div class="grid skills">
    <div class="card skill reveal"><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 3a3 3 0 0 0-3 3v.3A3 3 0 0 0 4 9v1a3 3 0 0 0 1 2.24V15a3 3 0 0 0 3 3h.5"/><path d="M14.5 3a3 3 0 0 1 3 3v.3A3 3 0 0 1 20 9v1a3 3 0 0 1-1 2.24V15a3 3 0 0 1-3 3h-.5"/><path d="M9.5 3v15M14.5 3v15"/></svg></div><h3>AI & Machine Learning</h3><small>CNN · Transformers · Keras · Model development</small></div>
    <div class="card skill reveal"><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg></div><h3>Computer Vision</h3><small>YOLOv3 · CNN · Image Classification · Object Detection</small></div>
    <div class="card skill reveal"><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="6" width="12" height="12" rx="1.5"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/></svg></div><h3>Hardware</h3><small>PC assembly · Troubleshooting · Embedded systems · Sensors</small></div>
    <div class="card skill reveal"><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M8 20h8M12 16v4"/></svg></div><h3>System Configuration</h3><small>Windows · Software setup · Networking · System deployment</small></div>
    <div class="card skill reveal"><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="1.5"/><circle cx="8.5" cy="8.5" r="1.1" fill="currentColor" stroke="none"/><circle cx="15.5" cy="15.5" r="1.1" fill="currentColor" stroke="none"/><path d="M8.5 9.6V13a1.5 1.5 0 0 0 1.5 1.5h3.2M15.5 14.4V11a1.5 1.5 0 0 0-1.5-1.5h-3.2"/></svg></div><h3>Circuit Design & PCB</h3><small>EAGLE CAD · Schematic design · PCB layout · PCB board fabrication</small></div>
    <div class="card skill reveal"><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5.5" rx="8" ry="3"/><path d="M4 5.5V12c0 1.66 3.58 3 8 3s8-1.34 8-3V5.5"/><path d="M4 12v6.5c0 1.66 3.58 3 8 3s8-1.34 8-3V12"/></svg></div><h3>Databases</h3><small>MySQL · PostgreSQL · Database design · Query optimization</small></div>
  </div>
</div>
</section>

<section id="languages">
<div class="container">
  <div class="section-head reveal"><div class="eyebrow">02b · Languages</div><h2>Programming languages.</h2></div>
  <div class="grid langs">
    <div class="card lang reveal"><div class="lang-badge php-badge">php</div><h3 style="font-size:.95rem">PHP</h3><small>Backend / Web</small></div>
    <div class="card lang reveal"><div class="lang-badge py-badge">Py</div><h3 style="font-size:.95rem">Python</h3><small>AI / ML / CV</small></div>
    <div class="card lang reveal"><div class="lang-badge js-badge">JS</div><h3 style="font-size:.95rem">JavaScript</h3><small>Web / Frontend</small></div>
    <div class="card lang reveal"><div class="lang-badge cs-badge">C#</div><h3 style="font-size:.95rem">C#</h3><small>Applications</small></div>
    <div class="card lang reveal"><div class="lang-badge c-badge">C</div><h3 style="font-size:.95rem">C</h3><small>Embedded / Systems</small></div>
    <div class="card lang reveal"><div class="lang-badge cpp-badge">C++</div><h3 style="font-size:.95rem">C++</h3><small>Systems / Embedded</small></div>
  </div>
</div>
</section>

<section id="projects">
<div class="container">
  <div class="section-head reveal"><div class="eyebrow">03 · Selected Work</div><h2>Projects that solve problems.</h2></div>
  <div class="grid projects">
    <article class="card project reveal">
      <h3>Pest & Disease Monitoring System (Thesis)</h3>
      <p>Thesis project: AI-powered agricultural monitoring for Lakatan banana farming that combines a CNN-based image classification model with a built-in AI chatbot for farmer support, fully integrated across hardware (camera/sensor capture) and software (detection, classification, and chat interface) in one system.</p>
      <span class="tag">CNN</span><span class="tag">AI Chatbot</span><span class="tag">Computer Vision</span><span class="tag">Smart Agriculture</span><span class="tag">Hardware + Software</span>
    </article>
    <article class="card project reveal">
      <h3>Fund Control System (IoT + Stock Management)</h3>
      <p>A hardware-and-software fund/stock control project: an Arduino Uno paired with a waterproof sensor handles the hardware side, while a web-based stock management system deployed on Vercel handles inventory and fund tracking — designed as an integrated embedded + web solution.</p>
      <span class="tag">Arduino Uno</span><span class="tag">Waterproof Sensor</span><span class="tag">Stock Management</span><span class="tag">Vercel</span>
    </article>
    <article class="card project reveal">
      <h3>Computer Vision Detection Projects</h3>
      <p>Hands-on experimentation with different computer vision approaches for object detection and image understanding using YOLOv3, CNN-based models, and Transformer architectures.</p>
      <span class="tag">YOLOv3</span><span class="tag">CNN</span><span class="tag">Transformers</span><span class="tag">Keras</span>
    </article>
    <article class="card project reveal">
      <h3>Hardware & System Configuration</h3>
      <p>Practical work involving computer hardware, operating system configuration, software installation, troubleshooting, device setup, and hardware-software integration.</p>
      <span class="tag">Hardware</span><span class="tag">Windows</span><span class="tag">Troubleshooting</span>
    </article>
    <article class="card project reveal">
      <h3>Robotics & Embedded Systems</h3>
      <p>Experience integrating microcontrollers, sensors, motors, communication, and intelligent processing into competition and automation projects.</p>
      <span class="tag">Arduino</span><span class="tag">Raspberry Pi</span><span class="tag">Sensors</span><span class="tag">Robotics</span>
    </article>
  </div>
</div>
</section>

<section id="research">
<div class="container">
  <div class="section-head reveal"><div class="eyebrow">04 · Research</div><h2>Published research.</h2></div>
  <div class="card research reveal">
    <div class="date">PUBLISHED RESEARCH</div>
    <h3 style="font-size:1.45rem;margin-top:9px">Pest and Disease Monitoring System for Banana Lakatan Farming Using CNN Algorithm</h3>
    <p style="margin-top:13px">
      Research focused on applying Convolutional Neural Networks to agricultural image analysis,
      with the goal of improving pest and disease monitoring for Lakatan banana farming.
    </p>
    <div style="margin-top:17px"><span class="tag">Agricultural AI</span><span class="tag">CNN</span><span class="tag">Image Classification</span><span class="tag">Smart Agriculture</span></div>
  </div>
  <div class="card reveal" style="margin-top:18px">
    <h3>Competitive Technology</h3>
    <p>Participated in regional robotics and technology competitions, including a Sumobot competition where the team achieved 1st Place in 2026.</p>
  </div>
</div>
</section>

<section id="experience">
<div class="container">
  <div class="section-head reveal"><div class="eyebrow">05 · Experience</div><h2>From classroom to real systems.</h2></div>
  <div class="timeline">
    <div class="card time-item reveal"><div class="date">CURRENT WORK</div><h3>Medical Records Archiver — Mindanao Medical Center, Inc.</h3><p>Currently handling medical records archiving, organization, and management at Mindanao Medical Center, Inc.</p></div>
    <div class="card time-item reveal"><div class="date">AI / MACHINE LEARNING</div><h3>AI & Computer Vision Development</h3><p>Developed and experimented with CNN, YOLOv3, Transformer-based approaches, and Keras for image analysis and computer vision applications.</p></div>
    <div class="card time-item reveal"><div class="date">HARDWARE & SYSTEMS</div><h3>Hardware & System Configuration</h3><p>Hands-on experience in hardware troubleshooting, computer setup, operating system configuration, software installation, and system support.</p></div>
    <div class="card time-item reveal"><div class="date">RESEARCH & ENGINEERING</div><h3>Research & Technology Projects</h3><p>Applied engineering concepts to agricultural AI, embedded systems, automation, robotics, and practical technology solutions.</p></div>
  </div>
</div>
</section>

<section id="contact">
<div class="container">
  <div class="section-head reveal"><div class="eyebrow">06 · Contact</div><h2>Let's build something useful.</h2></div>
  <div class="grid contact">
    <div class="card reveal"><h3>Joever L. Sayson</h3><p>Computer Engineering Graduate<br>AI · Machine Learning · Computer Vision<br>Hardware · System Configuration<br><br>📧 <a href="mailto:saysonjoever9@gmail.com" style="color:var(--accent)">saysonjoever9@gmail.com</a></p></div>
    <div class="card reveal"><h3>Open to opportunities</h3><p>Interested in roles and projects involving IT support, software, AI/ML, computer vision, hardware, systems, and technology research.</p></div>
  </div>
</div>
</section>
</main>

<footer><div class="container">© 2026 Joever L. Sayson · Computer Engineering Portfolio</div></footer>

<button class="ai" onclick="toggleAI()" aria-label="Open AI assistant">✦</button>
<div class="ai-panel" id="aiPanel">
  <h3>Joever AI Assistant</h3>
  <p>Ask about Joever's skills, projects, research, or experience.</p>
  <div class="ai-answer" id="aiAnswer">Hi! Ask me something about this portfolio.</div>
  <div class="ai-input"><input id="aiInput" placeholder="Ask a question..." onkeydown="if(event.key==='Enter')askAI()"><button onclick="askAI()">→</button></div>
</div>

<script>
const observer = new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')})
},{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));

function toggleAI(){document.getElementById('aiPanel').classList.toggle('show')}

function askAI(){
  const q=document.getElementById('aiInput').value.toLowerCase().trim();
  const a=document.getElementById('aiAnswer');
  if(!q)return;
  let answer="I can answer questions about Joever's portfolio, skills, projects, research, languages, and experience.";
  if(q.includes('skill')||q.includes('technology')){
    answer="Joever's focus includes AI/ML, Computer Vision, CNN, YOLOv3, Transformers, Keras, hardware troubleshooting, system configuration, circuit design/PCB layout with EAGLE, MySQL & PostgreSQL databases, and embedded systems.";
  }else if(q.includes('language')||q.includes('php')||q.includes('python')||q.includes('javascript')||q.includes('c#')||q.includes('c++')){
    answer="He programs in PHP, Python, JavaScript, C#, C, and C++.";
  }else if(q.includes('database')||q.includes('sql')||q.includes('mysql')||q.includes('postgres')){
    answer="He has experience working with MySQL and PostgreSQL databases.";
  }else if(q.includes('pcb')||q.includes('circuit')||q.includes('eagle')){
    answer="He builds circuits and designs PCB layouts and PCB boards using EAGLE CAD.";
  }else if(q.includes('fund')||q.includes('stock')||q.includes('vercel')||q.includes('arduino')){
    answer="One of his recent builds is a Fund Control System combining an Arduino Uno with a waterproof sensor for the hardware side, and a web-based stock management system deployed on Vercel for the software side.";
  }else if(q.includes('work')||q.includes('job')||q.includes('medical')){
    answer="He currently works as a Medical Records Archiver at Mindanao Medical Center, Inc.";
  }else if(q.includes('contact')||q.includes('email')||q.includes('gmail')){
    answer="You can reach Joever at saysonjoever9@gmail.com.";
  }else if(q.includes('project')){
    answer="Key projects include his thesis — a Pest and Disease Monitoring System for Banana Lakatan Farming using CNN with a built-in AI chatbot, combining hardware and software — plus a Fund Control System using Arduino Uno + a waterproof sensor with a Vercel-hosted stock management web app.";
  }else if(q.includes('research')||q.includes('paper')){
    answer="Joever is a published research author of a study on a CNN-based Pest and Disease Monitoring System for Banana Lakatan farming, which also features a built-in AI chatbot and combines hardware and software.";
  }else if(q.includes('education')||q.includes('graduate')){
    answer="Joever is a Computer Engineering graduate from Holy Trinity College in General Santos City.";
  }else if(q.includes('computer vision')||q.includes('yolo')||q.includes('cnn')||q.includes('transformer')){
    answer="His Computer Vision experience includes YOLOv3, CNN-based models, Transformer architectures, image classification, object detection, and Keras.";
  }else if(q.includes('hardware')||q.includes('system')){
    answer="He has hands-on experience with hardware troubleshooting, system configuration, software setup, embedded systems, sensors, circuit/PCB design, and hardware-software integration.";
  }
  a.textContent=answer;
  document.getElementById('aiInput').value='';
}

document.querySelector('.menu').addEventListener('click',()=>{
  document.querySelector('.nav-links').style.display =
    document.querySelector('.nav-links').style.display==='flex' ? '' : 'flex';
  if(window.innerWidth<=850){
    document.querySelector('.nav-links').style.position='absolute';
    document.querySelector('.nav-links').style.top='64px';
    document.querySelector('.nav-links').style.right='4%';
    document.querySelector('.nav-links').style.padding='18px';
    document.querySelector('.nav-links').style.background='#0b1220';
    document.querySelector('.nav-links').style.border='1px solid rgba(148,163,184,.15)';
    document.querySelector('.nav-links').style.borderRadius='14px';
    document.querySelector('.nav-links').style.flexDirection='column';
  }
});
</script>
</body>
</html>
'''

path = Path(__file__).resolve().parent / "joever_animated_ai_portfolio.html"
path.write_text(html, encoding="utf-8")
print(path)
