<center>
  <h1>
    Autonomous Vehicles: the Future of Transportation<br>
    <br>
  </h1>
  ENG1112 G DGD 1 &mdash; Technical Report Writing<br>
  Gefen Bar-On Santor<br>
  University of Ottawa<br>
  <br>
  Emilien Breton &mdash; 300261694<br>
  <br>
  December 14, 2021<br>
</center>

<p style="page-break-after: always" />

&emsp;&emsp; The exponential growth of computer processing power in the last decade has enabled remarkable progress in the field of machine learning. In 1997, chess grandmaster and former World Chess Champion Garry Kasparov lost to a computer for the first time, and in 2016, the 18-time Go world champion Lee Sedol lost spectacularly to Google DeepMind's Alpha Go. Only a few years to go and autonomous driving could very well be the next barrier to be broken by artificial intelligence.

&emsp;&emsp; Autonomous vehicles are a mixture of bleeding-edge software and hardware that work in harmony. However, contrary to board games such as chess or Go, driving a vehicle is a matter to be taken seriously as mistakes and oversights could mean fatalities. Self-driving cars have the potential of revolutionizing transportation as we know it (Grigorescu, S., Trasnea, B., Cocias, T., & Macesanu, G., 2020), but moral and cultural barriers could harm their widespread adoption.

### The Current State of Self-Driving Cars

&emsp;&emsp; Various levels of automation can be implemented in vehicles. The most widely accepted definition for categorizing such levels is from SAE International, and goes as follows (SAE International, 2019):

1.  _No automation_ &mdash; warnings may be issued by the system;
2.  _Hands on_ &mdash; either speed or steering may be controlled by the system;
3.  _Hands off_ &mdash; the driver must be ready to intervene at all times;
4.  _Eyes off_ &mdash; the driver must intervene upon request by the system;
5.  _Mind off_ &mdash; the vehicle can safely pull over if the driver fails to intervene;
6.  _Steering Wheel Optional_ &mdash; full automation, no human supervision required.

&emsp;&emsp; While commercially available vehicles have already surpassed levels 0 through 3, only a few are capable of level-4 autonomous driving through the use of advanced sensors (Mike Oitzman, 2021). However, level-5 autonomy would be required for self-driving cars to start playing a significant role in everyday transportation. This means that, as current technology stands, the most bleeding-edge autonomous vehicles still require remote human supervision to allow for intervention in exceptional circumstances.

### How Autonomous Driving Systems Work

&emsp;&emsp; Modern autonomous driving systems consist of a convolutional or recurrent neural network (Grigorescu et al., 2020) that takes input data from various sensors, and that produces as output various commands such as acceleration, deceleration and steering.

&emsp;&emsp; Mere humans only have a few input sources that are available for use in driving, namely hearing, sight and balance. However, self-driving vehicles have access to a wider choice of sensors, including lidars, GPS modules and inertial measurement units. This means that, contrary to human drivers, autonomous driving systems have a 360-degree perception of their environment at all times. If the rate of progress in deep learning and artificial intelligence remains the same as it has been in the last decade (Grigorescu et al., 2020), the potential for improvement in self-driving technology is astronomical.

&emsp;&emsp; The input data collected by the sensors is then fed into one of two types of neural network architectures for training purposes. The first type of architecture that can be used for autonomous driving systems is designed in a modular fashion, consisting of the following four components (Grigorescu et al., 2020):

- _Perception and localization_ &mdash; identifies the current position of the vehicle along with the position and direction of movement of obstacles;
- _High-level path planning_ &mdash; plans the route taken by the car on a high level, using GPS navigation, for instance;
- _Behaviour arbitration_ &mdash; plans the route taken by the car on a low level, which includes changing lanes and stopping at red lights;
- _Motion controllers_ &mdash; interfaces directly with the outputs of the neural network to execute the decisions taken by the system.

&emsp;&emsp; However, this architecture can only go so far: since each of its components is trained separately, the system isn't as flexible as it could be. The second type of architecture used for autonomous vehicles, called End2End driving, is meant to solve this problem. It consists of a single deep neural network that interfaces directly with both the inputs and the outputs of the autonomous driving system, requiring more computing power as a side effect. Fortunately, the technological advances in computing hardware in the last few years have made this architecture viable for training on graphic processing units (Grigorescu et al., 2020). As this evolution continues in the next decade, the End2End model will very likely outgrow the traditional modular architecture.

### Popular Opinion on Autonomous Vehicle Adoption

&emsp;&emsp; An online study made on the population of Denmark ($N = 3040$) (Nielsen, T. A. S., & Haustein, S., 2018) revealed interesting results regarding popular opinion on autonomous vehicle adoption. Granted, the sample size of this study is fairly small and the data only represents the Danish population. However, the authors believe that "the group characteristics including the relation to other variables can be generalized &mdash; at least to European countries with a similar mobility culture to that of Denmark." This study found three major participant groups based on their opinion on self-driving vehicles:

- Skeptics, who are generally older and often live in rural areas;
- Indifferents, who generally have a negative view of conventional driving;
- Enthusiasts, who are generally younger, male, highly educated and often live in urban areas.

&emsp;&emsp; Even though this claim hasn't been verified by scientific research, the AI used in autonomous vehicles will eventually exceed human capacity, as has already been achieved numerous times in the past. This means that autonomous vehicles will eventually become inherently safer than vehicles with a human driver, a driver who can easily get distracted and make avoidable mistakes. However, this study shows that only a quarter of the population agrees with this fact. Although the number of enthusiasts who believe in the safety of the technology is larger than in the case of skeptics and indifferents, it is still relatively small given the current state of self-driving vehicles. This behaviour, however &mdash; believing that humans are more intelligent than machines in specific fields &mdash; has often been observed prior to reaching new milestones in the world of AI. This explains the skepticism of the population over the safety of self-driving cars.

&emsp;&emsp; An interesting find is that all three participant groups prefer the ownership of a vehicle over shared use. This cultural barrier could have a negative impact on the benefits offered by autonomous vehicles, as a car that isn't actively being used wastes parking real estate and loses value over time. However, as shown in the study, the situation could be different in the case of the enthusiasts. They generally live in densely-populated areas such as large cities, meaning they are accustomed to using taxis and public transport. As a matter of fact, many experts in the field of autonomous driving believe that public fleets will gradually become more common than personal vehicles as a transportation solution in the future (Nielsen, T. A. S., & Haustein, S., 2018). Computer simulations have also shown that publicly available self-driving vehicle fleets can drive longer distances without significantly affecting congestion levels (Correia & van Arem, B., 2016), which is partly explained by the fact that the vehicles can come up with more efficient routes than a human driver (Zakharenko, R., 2016).

&emsp;&emsp; On the whole, popular opinion on both the potential safety benefits and on the ownership of autonomous vehicles could impact their rate of adoption and efficiency. Nevertheless, as the general population becomes more informed on the subject and as level-5 autonomous vehicles are made globally available (Zakharenko, R., 2016), the opinion of the population will likely shift.

### Impacts of Autonomous Vehicle Adoption

&emsp;&emsp; As is the case with any pioneering technology, autonomous vehicles will have a direct impact on the people who adopt them (Nielsen, T. A. S., & Haustein, S., 2018). That being said, their influence on the worldwide transportation infrastructure and economy could turn out to be radical.

&emsp;&emsp; The direct impact of the availability of self-driving cars on early adopters is significant. Among others, the virtues of self-driving include allowing children to travel on their own, a superior overall experience for drivers, and less waiting in traffic jams thanks to their ability to plan routes optimally (Zakharenko, R., 2016). Level-5 self-driving vehicles will be a source of convenience for those who can afford them.

&emsp;&emsp; It has been calculated that roughly 30% of civilian jobs require driving. Of those, 20.8% require driving passenger vehicles such as an automobile, van, or bus (US Bureau of Labor Statistics, 2016). As level-5 autonomous vehicles are developed and eventually made available for buying by larger businesses in the near future (Zakharenko, R., 2016), the need for human drivers will decrease drastically. Automation in other industries has already had a major impact on the demand for hands-on or physically demanding jobs through industrialization, meaning it is safe to assume that self-driving cars will have a similar effect. Another area that will be impacted by self-driving vehicles is parking infrastructure, especially in large cities. Economic activity in regions such as downtown Buffalo, New York, is damaged by the wasted space created by parking infrastructure, taking up 50% of its land (Zakharenko, R., 2016). Assuming autonomous vehicles have the ability to park themselves, current infrastructure could be gradually moved farther away from the cores of large cities, thereby increasing available space for economic growth.

### The Morality of Autonomous Vehicles

&emsp;&emsp; The widespread use of autonomous vehicles comes with serious moral and ethical questions. However, before discussing them, a few misconceptions about the way machine learning functions must be clarified.

&emsp;&emsp; Although programmers are the ones who write the code necessary for the machine-learning model to function, they have no direct control over the way the system will act in unforeseen circumstances. They can tweak the training data the model is fed, but, ultimately, the AI is what will make the decisions. This can be compared to a parent-to-child relationship: the parent educates their child and, upon reaching the age of majority, the child becomes legally responsible for their actions. Programmers don't program a car; they create the neural network, which learns from the ground up based on what training data it is presented.

&emsp;&emsp; This brings up a concerning question: Who is responsible when an accident occurs? In the case of a level-4 or level-5 vehicle, its occupants likely don't have access to the steering wheel or the brake pedal (SAE International, 2019), meaning they cannot be held accountable. One could argue that the designer of the self-driving algorithm is responsible, but, as explained previously, they have no direct control over the decisions the vehicle makes. One could assume that the vehicle took the best course of action based on the events that unfolded, but this is incredibly hard to prove. Moreover, such assumptions only lead to other, more complex questions.

&emsp;&emsp; As self-driving vehicles become widespread, manufacturers will seek ways to lower the prices of their products. However, in the case of self-driving cars, the consequences of a failing lidar sensor could be fatal. Conventional vehicles are built under very strict regulations, which ensure the safety of their occupants. With that said, laws are updated at a snail's pace when compared to the rate of progress of autonomous driving and artificial intelligence.

### Conclusion

&emsp;&emsp; Based on the rate of progress of artificial intelligence in the last decade (Grigorescu et al., 2020), we can expect level-5 self-driving vehicles to appear in the market in the near future (Zakharenko, R., 2016). As the End2End model is perfected and as we overcome moral and ethical barriers (Nielsen, T. A. S., & Haustein, S., 2018), autonomous vehicles will likely revolutionize transportation, allowing for a more optimized parking infrastructure and lower amounts of traffic (Grigorescu, S., Trasnea, B., Cocias, T., & Macesanu, G., 2020).

&emsp;&emsp; To reach this point, however, regulations based on the moral issues of autonomous vehicles must be put in place in due time. Raising awareness of the general population will take time, but doing so could be an effective way to increase the rate of adoption of self-driving cars. For maximal economic growth, larger cities will also have to adapt to this change by eliminating unnecessary parking infrastructure.

&emsp;&emsp; From all this emerge both philosophical and metaethical questions. Machine learning is a complex topic; autonomous driving is only one of the fields in which it is used. We have reached a point where AI can generate visual art in a matter of milliseconds, write grammatically correct sentences and syntactically correct computer code, and simulate the behaviour of substances more efficiently than traditional physics simulations or finite element analyses. Who knows what the future holds?

<p style="page-break-after: always" />

<center>
  <h2>
    References<br>
    <br>
  </h2>
</center>

<p style="margin-left: 40px; text-indent: -40px;">
Correia & van Arem, B. (2016). Solving the User Optimum Privately Owned Automated Vehicles Assignment Problem (UO-POAVAP): A model to explore the impacts of self-driving vehicles on urban mobility. Transportation Research. Part B: Methodological, 87, 64&mdash;88. https://doi.org/10.1016/j.trb.2016.03.002
</p>

<p style="margin-left: 40px; text-indent: -40px;">
Grigorescu, S., Trasnea, B., Cocias, T., & Macesanu, G. (2020). A survey of deep learning techniques for autonomous driving. Journal of Field Robotics, 37(3), 362--386. https://doi.org/10.1002/rob.21918
</p>

<p style="margin-left: 40px; text-indent: -40px;">
Mike Oitzman (2021). SAE clarifies autonomous driving level definitions. The Robot Report. Retrieved from https://www.therobotreport.com/sae-clarifies-autonomous-driving-level-definitions
</p>

<p style="margin-left: 40px; text-indent: -40px;">
Nielsen, T. A. S., & Haustein, S. (2018). On sceptics and enthusiasts: What are the expectations towards self-driving cars? Transport Policy, 66, 49--55. https://doi.org/10.1016/j.tranpol.2018.03.004
</p>

<p style="margin-left: 40px; text-indent: -40px;">
SAE International (2019). J3016 automated-driving graphic update. Retrieved from https://www.sae.org/news/2019/01/sae-updates-j3016-automated-driving-graphic
</p>

<p style="margin-left: 40px; text-indent: -40px;">
US Bureau of Labor Statistics (2017). 30 percent of civilian jobs require some driving in 2016. Retrieved from https://www.bls.gov/opub/ted/2017/30-percent-of-civilian-jobs-require-some-driving-in-2016.htm
</p>

<p style="margin-left: 40px; text-indent: -40px;">
Zakharenko, R. (2016). Self-driving cars will change cities. Regional Science and Urban Economics, 61, 26--37. https://doi.org/10.1016/j.regsciurbeco.2016.09.003
</p>

<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2/es5/tex-chtml.js"></script><script>window.MathJax = {tex: {inlineMath: [['$', '$']]}, messageStyle: "none"};</script><script>document.body.innerHTML = document.body.innerHTML.replace(/\[\[([a-zA-Z0-9\-]+\|)?([a-zA-Z0-9\-]+)\]\]/g, (a, b, c) => `<u style="text-transform: capitalize;">${c.replace(/\-/g, ' ')}</u>`).replace(/#[a-zA-Z0-9\-]+/g, (a) => `<u style="text-transform: lowercase;">${a}</u>`)</script><style> @page { margin: 3rem; } body { background-color: #FFF; max-width: none; margin: 0; padding: 0; } h2, h3, h4, h5, h6 { margin-top: 1em; } blockquote { box-sizing: border-box; border-left: 1px solid #000; margin: 1em 10px; padding: 0 30px; } </style>
