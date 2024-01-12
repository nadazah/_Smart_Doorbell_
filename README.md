# _Smart_Doorbell_

<p>This project was realized as part of the Cloud of Things module at Sup'Com, dedicated to enhance home and business 
security.
This project was done by:<p>
<ul>
 <li>Nada Zahra</li>
 <li>Aymen Houidi</li>
</ul>

## Context

The Smart Doorbell system aims to revolutionize home and business 
security by integrating face recognition technology with IoT because in today's digital age, traditional doorbells offer limited
security by merely alerting homeowners to visitors without identifying them. o address this, a proposed solution integrates facial recognition and user-activated cameras. 
Visitors pressing the doorbell activate the camera, capturing their image for identification. Unrecognized visitors prompt alerts for visual verification on the homeowner's mobile app, allowing access control. For recognized faces, instant notifications enhance security by providing real-time identity details.

## Demo

The mobile application can be tested on <a href="https://smartdb.ltn:8080" target="_blank">https://smartdb.ltn:8080</a>. You can view a demo of the mobile application here.

## Technologies

These are the technologies necessary to run this project:

<ul>
 <li>Wildfly preview 30.0.0 final</li>
<li>JDK 21</li>
<li>PWA</li>
<li>Node-red</li>
<li>Mosquitto Broker</li>
<li>Raspberry pi 4</li>
<li>Servo Motor actuator</li>
<li>Button actuator</li>
<li>Camera sensor</li>
<li>MongoDB</li>
</ul>

## Installation Guide
To run this application locally:

<ul>
    <li>Clone this repository.</li>
    <li>Import flows.json located in "IOT" on Node-red.</li>
    <li>Create a microprofile-properties.config folder in middleware/META-INF folder.</li>
    <li>Create a JWT keystore as mentioned in the user guide and store it in the jboss configuration directory.</li>
    <li>Package the middleware code into a single .war file with IntelliJ and place it in wildfly/standalone/deployments folder.</li>
    <li>Use "standalone.bat" to run Wildfly.</li>
    <li>Test the mobile application with <a href="https://smartdb.ltn:8080" target="_blank">https://smartdb.ltn:8080</a>.</li>
</ul>

## Deployment machine

With our school mail, we can get a 100$ voucher inside of Microsoft Azure. With this voucher, we can create a virtual machine capable of hosting the middleware, the mosquitto broker and the database. The virtual machine have the following characteristics:

Ram: 4 Gib
vCPUS: 2
Resource disk size: 8 GibDeployment machine
With our school mail, we can get a 100$ voucher inside of Microsoft Azure. With this voucher, we can create a virtual machine capable of hosting the middleware, the mosquitto broker and the database. The virtual machine have the following characteristics:

<ul>
    <li>Ram: 4 Gib</li>
    <li>vCPUs: 2</li>
    <li>Resource disk size: 8 Gib</li>
</ul>

## Certifications and grading

We have enabled HTTPS with letsencrypt TLS certificate with HSTS enabled as well, ensuring only secure connections are allowed to the middleware.



