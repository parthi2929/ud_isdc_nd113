This article tries to lay a foundational understanding for Bayes theorem. Especially what does it actually mean when you multiply two probabilities. This stems from Bayes theorem and we will explore it with an example.

<strong>Note</strong>: We will use the wonderful example provided in Quora, <a href="https://www.quora.com/What-is-an-intuitive-explanation-of-Bayes-Rule">here</a> and try to elaborate visually.

<strong>Problem</strong>: Given the weather forecast(WF) is rain, what is probability that it would actually rain in <strong>my area</strong>?

<strong>Assumptions</strong>: Out of 100 days rained, WF predicted correctly 90% of the time that it rained. Out of 100 days dry, WF predicted correctly 80% of the time, that it would be dry. In my area, out of 100 days, 10 days it would rain and 90 days would be dry.

We could visualize them as below. <em>Visualization is the key here in this article to understand, why the heck we "<strong>multiply</strong>" probabilities.</em>

<figure>
<img class="alignnone size-full wp-image-86" src="http://www.rparthiban.com/articles/wp-content/uploads/2018/03/2018-03-17_19h14_15.png" alt="2018-03-17_19h14_15" width="971" height="242" />
<figcaption align='center'>Figure 1</figcaption>
</figure>

If we try to apply WF for both rain and dry cases in my area, it would be something like this (not drawn to scale).

<div style="display: flex; justify-content: center;">
<figure>
<img src="http://www.rparthiban.com/articles/wp-content/uploads/2018/03/2018-03-17_19h14_271.png" alt="2018-03-17_19h14_27" width="442" height="237"/>
<figcaption align='center'>Figure 2</figcaption>
</figure>
</div>

For 10% of time raining in my area, WF would be 90% accurate to predict that it would rain. In other words, <strong>out of 10%</strong> days raining, WF would be <strong>90% of the time</strong>, correctly would predict as rain.

<span style="color: #0000ff;">90% out of 10% days raining is 90%(10%) = (0.9)(0.1) = 0.09 or 9%</span>

<span style="color: #0000ff;">Thus, 9% of the time in my area, its rains <strong>and</strong> WF would predict correctly as rain. </span>

That's it. This is how the multiplication is evolving out of our logic. Its not yet over.

From Figure 2, again, for 90% of time being dry in my area, WF would be wrong 20% of the time. That is WF would be predicting as rain, but it would be dry here. In other words, <strong>out of 90%</strong> days being dry, WF would be <strong>20% of the time</strong> wrongly predicting as rain.

<span style="color: #0000ff;">20% out of 90% days being dry is = (0.2)(0.9) = 0.18 or 18%</span>

<span style="color: #0000ff;">Thus, 18% of the time in my area, its dry, <strong>and</strong> WF would wrongly predict as rain.</span>

In terms of probability, if
$$
p(R_{\text{Act}})=\text{Probability of raining in my area}
\\
p(D_{\text{Act}})=\text{Probability of dryness in my area}
\\
p(R_{\text{WF}})=\text{Probability of WF as rain generally}
\\
p(D_{\text{WF}})=\text{Probability of WF as dry generally}\\p(R_{\text{Act}} \cap R_{\text{WF}}) = \text{Probability that it rains and WF also predicts rain} \\
p(D_{\text{Act}} \cap R_{\text{WF}}) = \text{Probability that it is dry and WF predicts rain}
$$

Then what we inferred in words above, can be expressed as,

$$
p(R_{\text{Act}} \cap R_{\text{WF}}) = (0.1)(0.9) = 0.09 \\
p(D_{\text{Act}} \cap R_{\text{WF}}) = (0.9)(0.2) = 0.18  \tag{1}  
$$
Putting it another way, out of 100 days in my area, {9 days it rains and WF also predicts as rain} and {18 days its dry and WF predicts as rain}.

Let us stop a moment and recall basic probability now:

$ \text {Probability of favourable outcome} = \frac{\text {No of favourable outcomes}}{\text {Total no of possible outcomes}} $

In our case,

$ \text {Total no of days its rain given WF says rain} = 9
\\
\text {Total no of days its dry given WF says rain} = 18
\\
\text {Total no of days either rain or dry given WF says rain} = 9 + 18 = 27$

Deploying that,

$
\\p(\text {actual rain given WF says rain}) = \frac{9}{9+18} = \frac{1}{3} = 0.33
\\
p(\text {actually dry given WF says rain}) = \frac{18}{9+18} = \frac{2}{3} = 0.66
$

We have a math notation for LHS..
$$p(R_{\text{Act}} \mid R_{\text{WF}}) = 0.33\\
p(D_{\text{Act}} \mid R_{\text{WF}}) = 0.66  \tag{2}
$$
Combining equations (1) and (2), we could thus see,
$$ p(R_{\text{Act}} \mid R_{\text{WF}}) =
\frac{p(R_{\text{Act}} \cap R_{\text{WF}})}{p(R_{\text{Act}} \cap R_{\text{WF}}) + p(D_{\text{Act}} \cap R_{\text{WF}})}
\\\\
p(D_{\text{Act}} \mid R_{\text{WF}}) =
\frac{p(D_{\text{Act}} \cap R_{\text{WF}})}{p(R_{\text{Act}} \cap R_{\text{WF}}) + p(D_{\text{Act}} \cap R_{\text{WF}})}$</p>
This in essence is Bayes' theorem. Note, we inferred visually, arrived at values and then combining observations, arrived at the formula. We did not apply formula and arrive at solution. Hope, thus this provides a good intuition to start with in Bayes' theorem.