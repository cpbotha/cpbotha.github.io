---
title: "Hivemind / Proximity: Distributed interactive personal lighting art project at AfrikaBurn 2018"
slug: "afrikaburn-2018-hivemind-proximity"
author: Charl P. Botha
date: 2024-08-10T23:10:00+02:00
draft: false
tags:
  - afrikaburn
  - arduino
  - c++
categories:
  - tech
type: "post"
ogimage: afrikaburn-2018.jpg
---

At AfrikaBurn 2018, the South African / Dutch theme camp Burniversity (that's us!) was again present and active with a
range of workshops and other learning experiences.

(Strangely, although [I wrote vaguely about our AB 2018 experience on this blog shortly after the
event](/2018/05/09/weekly-head-voices-141-albert-was-burning-really-hard/), I did not even mention this electronics
project, and now it's only taken 6 years to get around to the nerdy bits.)

That year, we had perhaps a bit too much energy and decided to design an electronic artwork, inspired by the fun we had
in 2017 with a giant bottle of helium, a bag of CR2032 button cell batteries and leds, and another bag full of
helium-grade balloons. (In short: On the less windy nights, we would inflate clusters of 4 to 5 balloons with helium,
each with a burning led inside, and attach the cluster to a theme camp member. Picture little clouds of illuminated
helium balloons floating above their humans as they were roaming over the Binnekring.)

I was the main hardware and software designer of our 2018 electronic artwork, eventually titled "Hivemind / Proximity",
and now the main topic of this post. Friend PK helped a lot in the earlier stages coming up with ideas, and building
test versions of my hardware and software designs, and later constructing the 7 production (haha) units, both at home
and in the desert, where we got additional help from more of our AfrikaBurn besties.

For some or other reason, we were less interested in taking photos and making movies, so I've had to scratch around to
find illustrative media for this post.

## The final product

In the end we had seven people (that's all of us) walking around the desert, each with a 25cm diameter circle of
coloured leds on their chest and a battery-powered arduino based controller on their waist that was in wireless
communication with all of the other units, with a range of a few hundred metres.

On each of the chest circles, each of the other team members was represented by a globally consistently coloured light
orbiting at a rate correlating with how close that team member was. The further away that team member went, the slower
their colour would rotate, until the units lost communication, at which point that member's light would start rotating
faster and faster in the opposite direction.

Once that team member came back in range, their light would start orbiting in the "right" direction, and would orbit
faster as they got closer.

This proximity visualization worked independently for each pair of team members, and hence for the group as a whole, as
you can hopefully imagine.

This early demo gives a good idea of what the animation looked like:
<video src="circling-leds.mp4" controls=yes />

The following extremely shaky video shows the assembled units, all happy as they are close to each other, shortly after
we did the final assembly in the raging Tankwa desert winds and dust. Here you can also see the effect of the diffuse
tubing that we put the leds in: <video src="circling-leds-assembled.mp4" controls=yes />

Finally, the following photo shows a partially assembled unit consisting of arduino, xbee shield, xbee radio and the
battery pack on the side with 4 x 1.5V AA batteries. Friend PK sourced a number of nylon dog treat bags, which were just
big enough to take the boards + battery pack and thus serve as our super professional production packaging. {{< figure
src="assembly.jpg" link="assembly.jpg" >}}

## Hardware

- [Robotdyn SAMD21 M0](https://robotdyn.com/samd21-m0.html): ARM Cortex M0 32bit Arduino clone. Fast enough to animate the LEDs while communicating with all other units and keeping track of their proximity.
- [XBee S2C XB24CAWIT-001 radio for 802.15.4](https://www.digi.com/products/models/xb24cawit-001): For wireless communication comms and RSSI feedback between units
- [ITEAD Studio XBee shield v1.1](https://vxlabs.com/2018/03/23/which-jumper-to-set-on-the-itead-xbee-shield-v1-1-for-use-with-a-3-3v-arduino/): To mount XBee onto the Arduino. I've linked to my vxlabs blog post about this unit, because it has important info re jumper configuration which can save you much time.
- [A few metres of 60/m WS2812B programmable LED strips (5V, 3 wire)](https://www.amazon.com/icever-WS2812B-MagicRGB-LED-Strip/dp/B0CFTP3S41/)
- [4 channel 3.3V to 5V logic level shifter (LEVEL-4P, BOB-12009)](https://www.robotics.org.za/LEVEL-4P): Convert 3.3V SAMD21 output to 5V required for programmable LEDs data line (durn...)

Getting all 7 of these units built and programmed, the final few in the desert at dusk of day 2 at the Burn, was quite a
challenge, requiring a gas powered soldering iron and liberal application of WvdL's (aka Broken Pipe) glue gun.

Especially the 3.3V to 5V level shifter added unnecessary complexity to the already precarious connection from power supply and controller board to the LED circle.

### The RSSI proximity "trick"

The SAMD21 is the electronic heart of the system.

It runs a special programme (see next section) that uses the XBee radio to broadcast a packet to the 802.15.4 wireless private area network (PAN), consisting of all of the units, every 1.5 seconds. It also listens, via the XBee radio, for any incoming packets.

Each incoming packet contains its sending ID.

Along with that packet, we also get the RSSI, which is an indicator of signal strength.

That RSSI is also a pretty good measurement of the *proximity* of the two units, and by proxy of their wearers.

If we are standing facing each other, the RSSI will be high. If I turn my back to you, the RSSI will be a bit lower. If I walk away from you, it will become lower still.

So, each unit maintains a list of IDs with the last known RSSI, and also when it last received a packet from that ID. It uses the RSSI to visualize proximity (that person's colour orbits faster the closer they are), and the age to detect person lost contact (orbits faster and faster in the other direction).

## Software

You can find the full commented [C++ source code for this project on my github](https://github.com/cpbotha/ab-hivemind).

Please do take a quick browse through the code as well, but here are some noteworthy learnings and observations:

- You can use this code for any number of wearable units (people), just remember to set `XBEE_SWARM_SIZE`.
- It took me so much time to get 100% reliable communication from the SAMD21 with the XBee. This was probably the
  biggest technical stumbling block. Besides documentation issues (see ITEAD linked post above), it the solution was to
  be super patient with the XBee. You'll see in the code, function `addressRead()`, that we just keep on trying, with
  generous waits, until we get a successful link.
- Like any good datavis practitioner, I opted for a color scheme from [ColorBrewer2](https://colorbrewer2.org/).
- As you can see in the main `loop()`, the paint loop is *lazy* and hence efficient, with three main event handlers
  triggering at different intervals of the arduino clock. This includes the 60fps LED animator, obviously triggering at
  the notorious 16ms interval. I used the fantastic `EVERY_N_MILLIS` macro from the even more fantastic [FastLED
  animation library](https://fastled.io/).

## Conclusion

In spite of desert soldering, glue-gun glue and duct tape holding everything together, all units worked in the pitch
dark of the desert, and were at times even used, quite effectively, to locate *utterly* lost team members in the
otherwise utterly reception-free environment.

If we ever do a v2 of this, we would produce a single board, with the smallest possible number of connections to
lighting and power.

Taking all of this into account, but especially thanks to our Burniversity peeps who were so positively curious and
willing to pour their energy into the difficult performance part, this was such a beautiful and worthwhile endeavour.
