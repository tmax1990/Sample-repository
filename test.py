import math
import sys
from os import rename
import requests
import json
import html_to_json

# print(sys.version)
# print(sys.executable)


def greet(who_to_greet):

    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet("World"))
# print (greet('Thomas'))
# r = requests.get("https://theprogrm.com/the-progrm-2-2022-week-8-22-1/")
# print(r.status_code)

# Save the page content as sample.html

html_string = """
<div class="entry-content clear" itemprop="text">

		
    <p style="padding-left: 40px;"></p>
<p data-tadv-p="keep"><strong>Welcome to Week 08</strong></p>
<p data-tadv-p="keep"><br></p>
<p data-tadv-p="keep"><strong><a href="https://youtu.be/OqdwISAAh7c" target="_blank" rel="noopener">Intro VIDEO</a></strong></p>
<p data-tadv-p="keep"><br></p>
<p data-tadv-p="keep">The 2022 Season is starting this week and I hope you are as pumped as we are.</p>
<p data-tadv-p="keep"><em>Before we do get started here are just a few details:</em></p>
<p data-tadv-p="keep"><br></p>
<p>Due to the start of The Open the overall volume this week will be slightly lower. If you need even more rest that is fine, we have indicated some of the pieces as optional. These are only for you to do it you are feeling good.</p>
<br>
<p>We know this can be a stressful time for some athletes. However it is important to remember we are here to help and guide you through this competition period.</p>
<br>
<p><b>Training Self Regulation:</b></p>
<p>Self-regulation is very important, especially during this time as 3 weeks can be a very long period. For example in our programming a Daily Max is a heavy lift, not necessarily an all out attempt at a new PR. If you feel good go heavier, if you don’t, don’t go up. The idea of a daily max is to work based on how you are feeling that day.</p>
<br>
<p>This is true in workouts as well. If we especially want you to go very hard or easy in a workout we will state this. However in cases where this is not stated you have to take responsibility of the effort you are putting in and take the workout accordingly.</p>
<br>
<p><b>No Open – No Problem.</b></p>
<p>We are aware that not everyone is prioritising The Open and is focused on training/other competitions. This is perfectly fine and we will still be focusing on your journey through this period. However we do recommend everybody does The Open workout at least once as it is the best test of your “fitness” at this period of time we can use. So go hard and try to do your best.</p>
<br>
<p>For those of you who are looking to prioritise The Open please read on:</p>
<br>
<p><b>There are some simple key factors to remember:</b></p>
<ol>
<li>If you can reduce any external stressors during the 3 weeks do so.</li>
<li>Sleep hygiene is crucial.</li>
<li>Maintain an optimal diet for the duration of The Open.</li>
</ol>
<br>
<p><b>Maintaining/Improving fitness during The Open</b></p>
<p>It is important to remember that we are entering a 3 week period of competition aka a long time! As you can imagine over 3 weeks it is actually easy to lose certain aspects of fitness that will possibly be important during the final week. Therefore we have at least 2 crucial training days mid week that are extremely important, here we need to maintain/improve our “fitness” (strength, conditioning, gymnastic capabilities). So make sure you are as fresh as possible for these sessions.</p>
<p>For athletes looking to optimise their Open performance we recommend doing the workouts at least twice. Friday/Monday. Please don’t look to attempt more than this in the first few weeks as it can effect performance in later weeks.</p>
<br>
<p><b>The Structure:</b></p>
<p><b>Thursday:</b> Active recovery.</p>
<p><b>Friday:</b> Open workout.</p>
<p><b>Saturday:</b> Normal training</p>
<p><b>Sunday:</b> Complete rest.</p>
<p><b>Monday:</b> Open workout repeat / or normal training.</p>
<p><b>Tuesday/Wednesday:</b> Normal training.</p>
<br>
<p>Note – if you want to do your first attempt on Saturday not Friday then we recommend “delaying” the week. The week would look like so:</p>
<br>
<p><b>Friday:</b> Active recovery. <b>Saturday:</b> Open workout. <b>Sunday:</b> Complete rest. <b>Monday:</b> Open workout repeat / or normal training. <b>Tuesday:</b> Active recovery day. <b>Wednesday/Thursday:</b> Normal)</p>
<br>
<p>Because we find out The Open workout the same time as you guys, Saturdays training (Training 6) will be updated based on what the announced workout is. Therefore the pdf document will be updated on Friday afternoon (13:00 Madrid Time) with the rest of the weeks training.</p>
<p data-tadv-p="keep"><br></p>
<p data-tadv-p="keep"><span style="color: #ff0000;"><strong>The Facebook Group:</strong></span></p>
<p data-tadv-p="keep">You should know by now – this is the group you need to be in:</p>
<p data-tadv-p="keep"><a href="https://www.facebook.com/groups/TheProgrm/" target="_blank" rel="noopener">https://www.facebook.com/groups/TheProgrm/</a></p>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<p data-tadv-p="keep">–</p>
<p data-tadv-p="keep">As always enjoy the week.</p>
<p data-tadv-p="keep"><em>The Progrm,</em></p>
<p data-tadv-p="keep"><em>Acta non Verba</em></p>
</div>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<p data-tadv-p="keep">


</p><div class="dkpdf-button-container" style=" text-align:right ">

    <a class="dkpdf-button" href="/the-progrm-2-2022-week-8-22-1/?pdf=48254" target="_blank"><span class="dkpdf-button-icon"><i class="fa fa-file-pdf-o"></i></span> Create PDF</a>

</div>





<p></p>
<h1 style="background-color: #aaa; color: white; padding: 10px;"><a id="training-1"></a>Training 1 (<a href="#training-2">2</a>, <a href="#training-3">3</a>, <a href="#training-4">4</a>, <a href="#training-5">5</a>, <a href="#training-6">6</a>)</h1>
<p data-tadv-p="keep"></p>
</div>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="section">
<div class="layoutArea">
<div class="column">
<h3><span style="font-size: 12pt; color: #ff9900;"><em>Session #1</em></span></h3>
<div class="layoutArea">
<div class="layoutArea">
<div class="column">
<div class="layoutArea">
<div class="column">
<div class="column">
<h2><strong><span style="color: #ff0000;">Weightlifting/Strength:</span></strong></h2>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<p><strong>Power Snatch + Hang Snatch + Snatch (Drop n Go)</strong></p>
<p>1. Build to a heavy single in the complex.</p>
<p><br><br>2. 9 Min EMOM at 90% of the complex:</p>
<p>Min 1: 1 Power Snatch<br>Min 2: 1 Hang Squat Snatch<br>Min 3: 1 Squat Snatch</p>
<br>
<p><strong>Snatch Deadlift</strong></p>
<p>3 x 5 @ 100-110% of the complex.</p>
<p><em>Not TnG, reset on the floor between reps. Use straps if needed.</em></p>
<br>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="column">
<p><strong>Back Squat</strong></p>
<div class="page" title="Page 2">
<div class="section">
<div class="layoutArea">
<div class="column">
<p>6 x 3 @ 70 – 80% of your most recent 1RM.</p>
<p><em>Aim to go every 90 seconds, use the same weight across all sets.</em></p>
<br>
</div>
</div>
</div>
</div>
<h2><span style="color: #ff0000;"><b>CrossFit:&nbsp;</b></span></h2>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<p><strong>2 rounds, each for time:</strong></p>
<p>25 Box Jump overs 24/20 inch<br>20 DB Front Squats 2 x 22.5/15kg</p>
<p>25 Push Ups&nbsp;<br>20 DB Hang Power Cleans 2 x 22.5/15kg<br>25 Burpees to target*</p>
<br>
<p><em>4 min rest between rounds.</em></p>
<p><em>*6 inches above fingertips when arms are fully extended</em></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="layoutArea">
<div class="column">
<div>
<h2></h2>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="column">
<h3><span style="font-size: 12pt; color: #ff9900;"><em>Session #2</em></span></h3>
<div class="layoutArea">
<div class="column">
<div class="column">
<div class="column">
<h2><b><span style="color: #ff0000;"><span style="caret-color: #ff0000;">Gymnastics</span>: (Optional)</span></b></h2>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<p><strong>Skill Development:</strong></p>
<p><em>Warm up with a band and PVC:</em><br>15 Straight arm pulldowns <a href="https://youtu.be/mAHKlSsYIl4" target="_blank" rel="noopener">Video</a><br>10 Hollow hold band pulls <a href="https://youtu.be/4cKp2jwxsnw" target="_blank" rel="noopener">Video</a><br>10 Banded glide kip</p>
<br>
<p><em>Then:</em><br>12 total reps, Glide kip swings for BMU</p>
<br>
<p><strong>Gymnastic Conditioning:</strong></p>
<p><strong>3 rounds for time:</strong></p>
<p>5 RMU</p>
<p>5 deficit HSPU</p>
<p>5 BMU</p>
<p>5 deficit HSPU</p>
<br>
<p><em>Make sure you do NOT RIP during the workout. Just break/stop if you are going to and look after the hands before The Open. For the HSPU choose a deficit you can fight for unbroken throughout.&nbsp;</em></p>
<br>
<h2><strong><span style="color: #ff0000;">Accessory:</span></strong></h2>
<p><strong>For quality:</strong></p>
<p>21-15-9</p>
<p>Ring rows&nbsp;<br>GHD Sit-up with Wall Ball 9/6 kg<br>Ring push-ups</p>
<br>
<p><em>For the ring rows hold yourself to a high standard. Elevate your feet if it feel easy.&nbsp;</em></p>
<br>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<h2><strong><span style="color: #ff0000;">Open recovery work:</span></strong></h2>
<p><span style="color: #000000;">1. 1 min foam rolling on the glutes both sides, then 10 reps of active pigeon each side.</span></p>
<p><span style="color: #000000;">2. 1 min foam rolling into the back of the shoulder, 30-60 sec passive hang from the bar.</span></p>
<p><span style="color: #000000;">3. 1 min foam rolling on lower back, then 10 each side.</span></p>
</div>
</div>
</div>
</div>
<div class="page" title="Page 5">
<div class="section">
<div class="layoutArea">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<p data-tadv-p="keep"><span style="font-size: 1rem;"></span></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<h1 style="background-color: #888; color: white; padding: 10px;"><a id="training-2" class="anchorhome"></a>Training 2</h1>
<p data-tadv-p="keep"></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<div class="page" title="Page 3">
<div class="page" title="Page 5">
<div class="section">
<div class="layoutArea">
<div class="page" title="Page 3">
<div class="page" title="Page 5">
<div class="section">
<div class="layoutArea">
<div class="page" title="Page 5">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 3">
<div class="page" title="Page 5">
<div class="section">
<div class="layoutArea">
<div class="page" title="Page 3">
<div class="page" title="Page 5">
<div class="section">
<div class="layoutArea">
<div class="page" title="Page 6">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 3">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 3">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 2">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 2">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 2">
<div class="layoutArea">
<div class="layoutArea">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<h3><span style="font-size: 12pt; color: #ff9900;"><em>Session #1</em></span></h3>
<div class="layoutArea">
<h2><span style="color: #ff0000;"><b>Weightlifting/Strength: (Optional)</b></span></h2>
<div class="page" title="Page 2">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 3">
<div class="section">
<div class="layoutArea">
<div class="column">
<p><strong>Deadlift</strong></p>
<p>1. Build to a heavy set of 6 (t<em>he reps must stay quick, no grinding</em>).</p>
<p>2. 3 x 6 @ 80% for speed. <em>Aim to go every 90 seconds, use the same weight across all sets.</em></p>
<br>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="layoutArea">
<div title="Page 3">
<div class="page" title="Page 2">
<div class="section">
<div class="layoutArea">
<div class="column">
<h2><strong><span style="color: #ff0000;">CrossFit:&nbsp;</span></strong><span style="color: #ff0000;"><b>(Optional)</b></span></h2>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<p><strong>3 Min AMRAP:</strong></p>
<p>10 DL 100/70kg<br>10 Box Jumps 24/20in</p>
<br>
<p><em>2 min Rest</em></p>
<br>
<p><strong>3 min AMRAP:</strong><br>10 TTB<br>10 Shoulder to overhead 50/35kg</p>
<br>
<p><em>2 min Rest</em></p>
<br>
<p><strong>3 min AMRAP:</strong><br>10 Alt DB Snatches 22.5/15kg<br>10 Burpees over DB (facing)</p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="layoutArea">
<div class="layoutArea">
<div class="layoutArea">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<h2><span style="font-size: 2.0588235294118rem;"></span></h2>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="layoutArea">
<h3><span style="font-size: 12pt; color: #ff9900;"><em>Session #2</em></span></h3>
<div title="Page 3">
<div class="layoutArea">
<h2><span style="color: #ff0000;"><b>CrossFit:</b></span></h2>
</div>
<div class="page" title="Page 3">
<div class="section">
<div class="layoutArea">
<div class="column">
<p><strong>For time:</strong></p>
<p>Buy in: accumulate 1 min freestanding HSH&nbsp;<span style="color: #00ccff;">/ wall facing HSH</span></p>
<br>
<p><em>3 rounds for time:&nbsp;</em></p>
<p>20m HSW&nbsp;</p>
<p>10m OH Walking lunge 22.5/15kg DB&nbsp;(Right arm)</p>
<p>10m OH Walking lunge 22.5/15kg DB (Left arm)</p>
<br>
<p>Cash out: 50 Pistol squats</p>
<br>
<p><em>Time cap: 18 min&nbsp;</em></p>
<br>
<p><i>Set up two cones 10m apart. For the HSW you have to walk back and forth. For this workout we want you to choose a steady pace throughout, no redlining. Make sure&nbsp;the pistols are warm before starting.</i></p>
<br>
</div>
<div title="Page 3">
<div class="page" title="Page 2">
<div class="section">
<div class="layoutArea">
<div class="column">
<h2><strong><span style="color: #ff0000;">Accessory:</span></strong></h2>
<p><strong>3 rounds for quality:</strong></p>
<p>6-8 Glute ham raises</p>
<p>20 Straight leg sumo DLs 50/35kg</p>
<br>
<p><strong>Finisher:</strong></p>
<p>100 Hollow Rocks*<br>*Every time you break: 20 sec Arch hold</p>
<br>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<h2><strong><span style="color: #ff0000;">Open recovery work:</span></strong></h2>
<p>1. 1 min foam rolling on the glutes both sides, then 10 reps of active pigeon each side.</p>
<p>2. 1 min foam rolling into the back of the shoulder, 30-60 sec passive hang from the bar.</p>
<p>3. 1 min foam rolling on lower back, then 10 lying Windmills each side.</p>
</div>
</div>
</div>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<div class="page" title="Page 3">
<div class="page" title="Page 5">
<div class="section">
<div class="layoutArea">
<div class="column">
<p data-tadv-p="keep"></p>
<h1 style="background-color: #666; color: white; padding: 10px;"><a id="training-3" class="anchorhome"></a>Training 3</h1>
<p data-tadv-p="keep"></p>
</div>
</div>
</div>
</div>
</div>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<h3><span style="font-size: 12pt; color: #ff9900;"><em>Session #1</em></span></h3>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div class="column">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<h2><b><span style="color: #ff0000;">Weightlifting/Strength:</span></b></h2>
</div>
</div>
</div>
<div class="section">
<div class="layoutArea">
<div class="page" title="Page 3">
<div class="page" title="Page 5">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 3">
<div class="section">
<div class="layoutArea">
<div class="column">
<p><strong>Clean and Jerk</strong></p>
<p>Build to a technical sound single, roughly 80-90% of your all time 1RM.</p>
<br>
<p><strong>Front Squat Complex</strong></p>
<p>1. Find your daily max in: <em>3 second paused Front squat + Front squat.</em><br>2. Do five additional front squat singles without the pause at the heaviest weight you managed in the complex.</p>
<br>
<p><strong>&nbsp;Strict Press</strong><br>1. Find your daily 2RM.<br>2. 3 x 2 at 90% of today’s heavy 2RM.</p>
<br>
<h2><strong><span style="color: #ff0000;">CrossFit: (<span style="caret-color: #ff0000;">Optional)</span></span></strong></h2>
<p><strong>8 min AMRAP:</strong></p>
<p>50 Double unders<br>10 GTOH 45/30kg</p>
<br>
<p><em>Then into:</em><br><strong>4 minutes to find a daily max in Clean + Jerk.</strong></p>
<p><i>Again we are looking for a technically sound lift after the workout, this doesn’t&nbsp;have to be a lifetime PR.&nbsp;This should be a similar&nbsp;weight you achieved in the morning, roughly 80-90% of your all time 1RM.</i></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div title="Page 1">
<div class="layoutArea">
<div class="column">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="page" title="Page 3">
<div class="layoutArea">
<div class="column">
<p><span style="color: #000000; font-family: Oswald, sans-serif; font-size: 2.0588235294118rem;"></span></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="page" title="Page 3">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 6">
<div class="section">
<div class="layoutArea">
<h3><span style="font-size: 12pt; color: #ff9900;"><em>Session #2</em></span></h3>
<h2><strong><span style="color: #ff0000;">CrossFit: (Optional)</span></strong></h2>
<div title="Page 1">
<div class="page" title="Page 3">
<div class="section">
<div class="layoutArea">
<div class="column">
<p><strong>For Reps:</strong></p>
<p>5 Min row</p>
<p>2 min Burpees over rower (lateral)</p>
<br>
<p><em>2 min rest&nbsp;</em></p>
<br>
<p>5 Min ski</p>
<p>2 Min TTB</p>
<br>
<p><em>2 min rest</em></p>
<br>
<p>5 Min Bike (erg) / Run</p>
<p>2 Min Air squats</p>
<br>
<p><em>The idea of the workout is to maintain a comfortable pace on the row/ski/bike or run. Then throughout the gymnastic movements the focus is staying technically proficient.</em></p>
</div>
</div>
</div>
</div>
<br>
</div>
<div class="page" title="Page 3">
<div class="section">
<div class="layoutArea">
<div class="column">
<h2><strong><span style="color: #ff0000;">Accessory:</span></strong></h2>
<p><strong>TGU + OHS</strong></p>
<p>1.&nbsp;Build to a daily max in TGU + OHS <a href="https://youtu.be/FWyBt73xqOs" target="_blank" rel="noopener">Video</a></p>
<p>2. Drop down to 24/26kg and perform 8 reps of the complex each arm&nbsp;</p>
<br>
<p><strong>For Load:</strong><br>10 – 8 – 4 – 2<br>DB Bench Press</p>
<p>Strict Pull-up</p>
<br>
<p><em>For the Bench presses choose a weight that is challenging, but you can manage unbroken.&nbsp;</em></p>
<p><em>Be strict with yourself in in the pull-ups. Stay in hollow and keep the legs in front of the bar, don’t let them “swing”</em>.</p>
<br>
</div>
<h2><strong><span style="color: #ff0000;">Open recovery work:</span></strong></h2>
<p>1. 1 min foam rolling on the glutes both sides, then 10 reps of active pigeon each side.</p>
<p>2. 1 min foam rolling into the back of the shoulder, 30-60 sec passive hang from the bar.</p>
<p>3. 1 min foam rolling on lower back, then 10 lying Windmills each side.</p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="page" title="Page 3">
<div class="section">
<div class="layoutArea">
<div class="column">
<p data-tadv-p="keep"></p>
<h1 style="background-color: #444; color: white; padding: 10px;"><a id="training-4" class="anchorhome"></a>Training 4</h1>
<p data-tadv-p="keep"></p>
<h2><b><span style="color: #ff0000;">Open&nbsp;<span style="caret-color: #ff0000;">Preparation: (Optional)</span></span></b></h2>
<div class="page" title="Page 4">
<div class="section">
<div class="layoutArea">
<div class="column">
<p><i>The focus of this session is purely to get the body moving&nbsp;and feeling fresh, before the first Open attempt tomorrow. If you are an athlete that prefers to&nbsp;have a full rest for T4 that is absolutely fine.</i></p>
<br>
</div>
</div>
<div class="page" title="Page 4">
<div class="section">
<div class="layoutArea">
<div class="column">
<p><strong>Grease the groove:*</strong></p>
<p>3 min Ski Erg<br>30 sec Bar hang</p>
<p>10 Cossack squats (fight to stay as low and upright as possible) <a href="https://youtu.be/S-sjuVAvz9E" target="_blank" rel="noopener">Video</a><br>3 min Row</p>
<p>30 sec HSH (if possible free standing, if not wall facing)</p>
<p>10 Sumo stance air squats</p>
<p>3 min Bike<br>30 sec Bar hang</p>
<p>10 alternating lunge with OH reach <a href="https://youtu.be/vlEy2uAmsss" target="_blank" rel="noopener">Video</a></p>
<br>
<p><em>*easy, sustainable pace. Just to move the body, loosen up and get the blood flowing.&nbsp;</em></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<h2></h2>
</div>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<h2><strong><span style="color: #ff0000;">The Progrm Recovery:</span></strong></h2>
<p data-tadv-p="keep"><em>The focus of this session is an “easy recovery” to not only improve your movement but to get your body feeling fresh before your next training session begins.</em></p>
<p data-tadv-p="keep"><br></p>
<p><strong>18 min EMOM:</strong></p>
<p>Min 1: Close grip hang</p>
<p><span style="font-weight: 400;">Min 2: German hang <a href="https://youtu.be/vAaQX-gK4xQ" target="_blank" rel="noopener">Video</a>&nbsp;/ Kneeling <a href="https://youtu.be/BjTNAq1Cd-Q" target="_blank" rel="noopener">Video</a></span></p>
<p><span style="font-weight: 400;">Min 3: Windmill with light KB (Alternate the minutes R + L arms) <a href="https://youtu.be/fARgZSLhaGk" target="_blank" rel="noopener">Video</a></span></p>
<p><span style="font-weight: 400;">Min 4: Rolling feet together deck squat <a href="https://youtu.be/GSUq18ayUSk" target="_blank" rel="noopener">Video</a></span></p>
<p>Min 5: Straddle stretch <a href="https://youtu.be/ikfzMlcPWdg" target="_blank" rel="noopener">Video</a></p>
<p><span style="font-weight: 400;">Min 6: Active hip extension <a href="https://youtu.be/yp1gXoDyH_0" target="_blank" rel="noopener">Video</a></span></p>
</div>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<p data-tadv-p="keep"></p>
<h1 style="background-color: #222; color: white; padding: 10px;"><a id="training-5" class="anchorhome"></a>Training 5</h1>
<p data-tadv-p="keep"></p>
</div>
<h2><strong><span style="color: #ff0000;">CrossFit Open 22.2</span></strong></h2>
<p><strong>15 min AMRAP:&nbsp;</strong></p>
<p>3 Wall walks</p>
<p>12 Alt DB snatches 1×22.5/15kg&nbsp;</p>
<p>15 Box jump overs 24/20in&nbsp;</p>
<br>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<p><a href="https://theprogrm.com/crossfit-open-22-1/"><strong><i>Our Strategy</i><i> Guide</i></strong></a>&nbsp;</p>
<br>
<p><em>We do recommend everyone to do the Open workout, however if this isn’t a focus of yours just perform is as any other workout.&nbsp;</em></p>
<div class="page" title="Page 5">
<div class="section">
<div class="layoutArea">
<div class="column">
<h2></h2>
<h3><span style="font-size: 12pt; color: #ff9900;"><em>Session #2</em></span></h3>
<h2><strong><span style="color: #ff0000;">Weightlifting / Strength:</span></strong></h2>
<p><b>Deadlift</b></p>
<p>1. Build to a heavy 3RM <em>(Keep the reps quick).</em></p>
<p>2. 6 x 1 at the same weight EMOM.</p>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<p><b>Good mornings</b></p>
<p>Build to a heavy 8RM.</p>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<p><b>Dimmel deadlift</b></p>
<p>3 x 20 <a href="https://youtu.be/4FXrxOzf0jA" target="_blank" rel="noopener">Video</a></p>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<p><b>Banded KB swings</b></p>
<p>3 x 20 banded Russian KB swings <a href="https://youtu.be/QKAAdDqTKlE" target="_blank" rel="noopener">Video</a></p>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<h2><strong><span style="color: #ff0000;">CrossFit:</span></strong></h2>
<p><b>6 x 90 sec on – 90 sec off:</b></p>
<p>25/20 cal row</p>
<p>Max D-ball cleans in the remaining time 60/45kg</p>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<h2><strong><span style="color: #ff0000;">Accessory:</span></strong></h2>
<p><b>3 rounds for quality:&nbsp;</b></p>
<p>4-7 Bottom half TTB</p>
<p>4-7 Top half TTB</p>
<p>4-7 Full TTB</p>
<p><em>Hold yourself to a high standard, these should be performed _strict_. Goal is to choose a rep scheme that you can go unbroken throughout the set for. Rest as needed between sets.&nbsp;</em></p>
</div>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<h2><strong><span style="color: #ff0000;">Open recovery work:</span></strong></h2>
<p>1. 1 min foam rolling on the glutes both sides, then 10 reps of active pigeon each side.</p>
<p>2. 1 min foam rolling into the back of the shoulder, 30-60 sec passive hang from the bar.</p>
<p>3. 1 min foam rolling on lower back, then 10 lying Windmills each side.</p>
</div>
</div>
</div>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<div class="page" title="Page 1">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 1">
<div class="page" title="Page 2">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="layoutArea">
<div class="page" title="Page 2">
<div class="section">
<div class="layoutArea">
<div class="column">
<div class="page" title="Page 6">
<div class="section">
<div class="layoutArea">
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<p data-tadv-p="keep"></p>
<h1 style="background-color: #000; color: white; padding: 10px;">Training 6</h1>
<p data-tadv-p="keep"></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<h3><span style="font-size: 12pt; color: #ff9900;"><em>Session #1</em></span></h3>
</div>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<h2><span style="color: #ff0000;"><strong>Weightlifting / Strength:</strong><br></span></h2>
<p><b>Power Clean from blocks (just above knees)</b></p>
<p>1. Find todays technical heavy single with a 2 sec pause in the catch.</p>
<br>
<p>2. 10 min EMOM: 1 clean pull + 1 clean at 80-90% of todays heavy 1RM.</p>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<p><b>Front squats</b></p>
<p>5 x 3 @70-80%. Go every 2:30&nbsp;</p>
</div>
<p><em>Tempo: 3 sec lowering, 1 sec pause in the bottom, explosive stand-up&nbsp;</em></p>
<p>Focus on keeping your torso upright and really fight for a quick stand-up.&nbsp;</p>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
</div>
<h2><strong><span style="color: #ff0000;">CrossFit:</span></strong></h2>
<p><strong>7 rounds for time:</strong></p>
<p>15 GHD Sit ups<br>15 GHD Back Extensions<br>10 Front Squats 45/30kg<br>10 Alternating Front Rack Lunges 45/30kg</p>
<br>
<p><em>Make sure to warm up the lower back well before starting this piece. Aim to settle in to a pace from the beginning.&nbsp;&nbsp;</em></p>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<h2><strong><span style="color: #ff0000;">Accessory:&nbsp;</span></strong></h2>
<p><b>Bullet-proofing shoulders.</b></p>
<p><strong>4 rounds for quality:&nbsp;</strong></p>
<p>1-3 Skin the cat <a href="https://youtu.be/we8r0cx4_xs" target="_blank" rel="noopener">Video</a></p>
<p>6-8 Windmills, each arm <a href="https://youtu.be/fARgZSLhaGk" target="_blank" rel="noopener">Video</a>&nbsp;</p>
<p>12-15 Reverse flies <a href="https://youtu.be/OJ_ELSMfokM" target="_blank" rel="noopener">Video</a></p>
<p>10 Ring rows&nbsp;</p>
</div>
</div>
</div>
<h2></h2>
<h3><span style="font-size: 12pt; color: #ff9900;"><em>Session #2</em></span></h3>
<h2><span style="color: #ff0000;"><b>Gymnastics:</b></span></h2>
<p><b>Skill Development:</b></p>
<p>1. 3 x 10 Hollow hold banded pulls <a href="https://youtu.be/4cKp2jwxsnw" target="_blank" rel="noopener">Video</a></p>
<p>2. 5 Jump to hollow for BMU <a href="https://youtu.be/UGicn4nVIOg" target="_blank" rel="noopener">Video</a></p>
<p>3. 5 Hip to bar for BMU <a href="https://youtu.be/QQgCRyyNZGE" target="_blank" rel="noopener">Video</a></p>
<p>4. 3 x 1-3 Bar kick backs <a href="https://youtu.be/c1SmysWsNvQ" target="_blank" rel="noopener">Video</a>&nbsp;</p>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<p><b>Gymnastic Conditioning: </b></p>
<p><strong>For time:*</strong></p>
<p>40 BMU</p>
<p>*Every time you break: 200m Ski&nbsp;</p>
<br>
<p><em>Do NOT rip your hands, stop if you are getting close.&nbsp;</em></p>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<h2><b><span style="color: #ff0000;"><span style="caret-color: #ff0000;">Conditioning</span>:</span></b></h2>
<p><strong>Concept 2 Bike&nbsp;</strong></p>
<p>3 x 8km with cadence change / 4 minutes rest between.</p>
<br>
<p class="light">In each piece change the cadence every 2km:</p>
<p class="light">1st @ 70 rpm. 2nd @ 80 rpm. 3rd @ 70 and 4th @ 85.</p>
<br>
<p>If only a Rower available 1/2 the distance and vary stroke rates every 1km: 1st @24. 2nd @28. 3rd @ 24. 4th @ 30</p>
<p><span style="color: #ff0000;"><span style="color: #333333;"><br></span></span></p>
<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">
<h2><strong><span style="color: #ff0000;">Open recovery work:</span></strong></h2>
<p>1. 1 min foam rolling on the glutes both sides, then 10 reps of active pigeon each side.</p>
<p>2. 1 min foam rolling into the back of the shoulder, 30-60 sec passive hang from the bar.</p>
<p>3. 1 min foam rolling on lower back, then 10 lying Windmills each side.</p>
<p data-tadv-p="keep"></p>
</div>


<p></p>
<!-- AI CONTENT END 1 -->

    
    
        </div>

"""

output_json = html_to_json.convert(html_string)
# print(output_json)

print(type(output_json))

data = json.dumps(output_json, indent=2)


print(data)
