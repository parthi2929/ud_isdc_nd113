<em>Note</em>: This article is an extension of "<a href="https://parthibanrajendran.wordpress.com/2018/03/17/0-bayes-theorem-intuitive-foundation/">Intuitive Approach to Bayes theorem - Part 1</a>", which is not strictly needed but could be immensely helpful especially when we multiply probabilities here.

Recently I enrolled for "Introduction to Machine learning" in Udacity. In lesson 2, chapter 24, the author explains about how Bayes theorem works out. Though the example was simple, it was still difficult to comprehend, because I already lost touch with probability (had studied in college days more than a decade back), not yet refreshed statistics any time later so was trying other sources to understand it intuitively. I tried "Khan academy" next, which beautifully started the explanation with visual examples, but at one point, they too simply failed to explain an important step, which was crucial for the overall understanding. Many other links via online search also did not help much. Stack overflow finally came to rescue clearing the specific doubt which then helped me comprehend the complete picture. I then wanted to take note of this understanding in detail for future reference and also share with the world which might find it useful.

<a href="https://youtu.be/EL5z2lUuxY4" target="_blank" rel="noopener nofollow">Bayes theorem link in Udacity</a> : How is it 8.3%?

<a href="https://www.khanacademy.org/math/ap-statistics/probability-ap/stats-conditional-probability/v/bayes-theorem-visualized" target="_blank" rel="noopener nofollow">Conditional probability with Bayes' Theorem: </a>Why the tree should be balanced in 2nd example of 2 fair coins and 1 biased coin?

<a href="https://math.stackexchange.com/questions/2680957/what-is-pbiased-coin-given-heads-in-2-fair-coin-1-biased-coin-experiment" target="_blank" rel="noopener nofollow">My blocking point/doubt in detail.</a>

I will try explaining 2 examples used in above videos, and how we could approach them intuitively as per my understanding.

<strong>Example 1 (Khan academy): </strong>There are 2 fair coins (fair coin = 1 head and 1 tail), and 1 biased coin (which is when flipped gives heads 2/3rd of the time, and tail 1/3rd of the time) in a bag. Now one picks up a coin from the bag, and flips it. Given that it is heads, what is the probability that the coin is biased?

Let us assume,

<strong>p(B)</strong> = probability of biased coin
<strong>p(B/H)</strong> = probability of biased coin, given its Heads.
<strong>p(H)</strong> = probability of coin being Heads
<strong>p(H/B)</strong> = probability of coin being Heads, given its biased
<strong>p(B and H)</strong> = probability of coin being both biased and heads.

Let us try to visualize with a tree diagram (unfolding of events, with possible outcomes and their probabilities).

During 1st event, when a coin is picked up from the bag, it could be either Fair or Biased. Since there are 2 Fair coins and 1 Biased coin, we could visualize it as follows with probabilities assigned to each.

<div style="display: flex; justify-content: center;">
<figure>
<img src="http://www.rparthiban.com/articles/wp-content/uploads/2018/03/2018-03-08_15h31_11.png"/>
<figcaption align='center'>Figure 1</figcaption>
</figure>
</div>

<p style="text-align: left;" align="”center”">
p(B) = probability of coin being biased
p(F) = probability of fair coin</p>
<p align="”center”">Since 2 fair coins,</p>

$$
p(F)={\frac {\text {Number of fair coins}} {\text {Total number of coins}}} = \frac{2}{3}\\\\
p(B)={\frac {\text {Number of biased coins}} {\text {Total number of coins}}} = \frac{1}{3}
$$
<p align="”center”">Note that,obviously, as output is either biased or fair coin</p>

$$
p(F) + p(B) = \frac{2}{3} + \frac{1}{3} = 1
$$
<p align="”center”">This total probability being 1 should be satisfied from all branches of any node in the tree.</p>
<p align="”center”">This is not yet over. A coin is picked up from 3 sets. Thus we derive one more level as follows.</p>

<div style="display: flex; justify-content: center;">
<figure>
<img src="http://www.rparthiban.com/articles/wp-content/uploads/2018/03/2018-03-08_19h29_10.png"/>
<figcaption align='center'>Figure 2</figcaption>
</figure>
</div>

Once a coin is picked up out of "FFB" set, if picked up coin is "F", then remaining set for further possibility has only "FB". And outcome out of this remaining set could be either "F" or "B", each having equal chance, thus halved probability.

Similarly, once "B" is picked up, with remaining set containing "FF", the outcome is always only a "F" with 100% certainty. This is also depicted above as probability being 1.

Note, now we have multiple probabilities for p(F) and p(B). This is now mainly because we did not just have 2 coins to start with "FB", but "FFB", thus this additional level needed.

In same way, now we extend to the H and T possibilities of each end node. Note the p(H) and p(T) for B in particular where, heads has 2/3rd times chance of showing up.

<div style="display: flex; justify-content: center;">
<figure>
<img src="http://www.rparthiban.com/articles/wp-content/uploads/2018/03/2018-03-08_19h36_08.png"/>
<figcaption align='center'>Figure 3</figcaption>
</figure>
</div>


That is it. We have drawn a tree of all possible outcomes, with associated probabilities.

Note that, <strong>p (B and H) = p (H and B)</strong>, both are same. That is,

p( final outcome being both biased coin with heads) = p(final outcome of heads being a biased coin).

Note that p( A and B) is not p (A | B). Both mean different, with latter being conditional probability.

From Figure 3, p (B and H) is the highlighted path, thus we multiply their probabilities in the path.

<div style="display: flex; justify-content: center;">
<figure>
<img src="http://www.rparthiban.com/articles/wp-content/uploads/2018/03/2018-03-08_19h45_28.png"/>
<figcaption align='center'>Figure 4</figcaption>
</figure>
</div>

$p(\text {B and H})= \frac{2}{3}. \frac{1}{2}.\frac{2}{3} = \frac{4}{18} = \frac{2}{9}$

Recall the question, <em>"Given that picked up coin is heads, what is the probability that the coin is biased?"</em>

That is, <strong>given</strong> H, what is p(B). In other words, what is <strong>p(B|H)</strong>?

Notice, here the prior event is "heads" being picked up. Let us calculate all the probabilities of heads being picked up. That is <strong>p(H)</strong>.

<div style="display: flex; justify-content: center;">
<figure>
<img src="http://www.rparthiban.com/articles/wp-content/uploads/2018/03/2018-03-08_20h03_04.png"/>
<figcaption align='center'>Figure 5</figcaption>
</figure>
</div>

$p(\text {H})= \frac{2}{3}. \frac{1}{2}.\frac{1}{2} + \frac{2}{3}.\frac{1}{2}.\frac{2}{3} + \frac{1}{3}.1.\frac{1}{2} = \frac{2}{12} + \frac{4}{18} + \frac{1}{6} = \frac{15}{27}= \frac{5}{9}$

Coming back to <strong>p(B and H)</strong>, it can be interpreted as

p( final outcome being <span style="color: #0000ff;">both biased coin and heads</span>) = p (outcome of <span style="color: #0000ff;">all possible heads scenario</span>) x p (outcome of getting <span style="color: #0000ff;">biased coin, given heads</span> has occurred).

$p(\text {B and H})= p(\text {H}) . p(\text {B} \mid \text {H})$

Re read. This is the very crux of our solution. The latter in above equation can now be readily derived.

$p(\text {B} \mid \text {H}) = \frac{p(\text {B and H})}{p(\text {H})} = \frac{2}{9} . \frac{9}{5}= \frac{2}{5}$

Thus, the probability of getting biased coin, given heads occurred is $\frac{ 2 }{ 5 }$. This conforms with Khan academy's answer as well (which is $\frac{ 4 }{ 10 }$). Note that even though I have not yet understood, why the tree (which is different) in Khan academy's video has to be balanced, I am now able to derive the same solution via a slightly different approach.

<strong>Example 2 (Udacity): </strong>Suppose there is a known statistics that 1% of population gets cancer. When we then test them, there is 90% chance, test is positive, if that person being tested has cancer. Similarly, there is also 90% chance, test is negative, if that person being tested does not have cancer. As first event, we test a person, and the result is positive. Now what is the probability that the person has cancer?

Let us assume,

p(C) = probability of cancer
p(+/C) = probability of test being +, <strong>given</strong> the person has cancer.
p(+) = probability of test being +
p(C/+) = probability of person having cancer, <strong>given</strong> the test is positive
p(C and +) = probability of person having cancer and test being positive.

Visualizing in tree diagram, just like previous problem..


<div style="display: flex; justify-content: center;">
<figure>
<img src="http://www.rparthiban.com/articles/wp-content/uploads/2018/03/2018-03-08_21h27_41.png"/>
<figcaption align='center'>Figure 1</figcaption>
</figure>
</div>

Rephrasing the question, what is the probability of person having cancer, <strong>given</strong> the test conducted on him is positive. In other words, what is <strong>p(C/+)</strong>.

From the tree, we can derive the probability of person having cancer and test being positive, that is <strong>p(C and +)</strong>

<div style="display: flex; justify-content: center;">
<figure>
<img src="http://www.rparthiban.com/articles/wp-content/uploads/2018/03/2018-03-08_21h31_24.png"/>
<figcaption align='center'>Figure 2</figcaption>
</figure>
</div>


<p style="text-align: center;"><strong>p(C and +)</strong> = (0.01) (0.9) = 0.009</p>
From the tree, we can also derive probability of all outcomes of test being positive, that is <strong>p(+)</strong>


<div style="display: flex; justify-content: center;">
<figure>
<img src="http://www.rparthiban.com/articles/wp-content/uploads/2018/03/2018-03-08_21h34_52.png"/>
<figcaption align='center'>Figure 3</figcaption>
</figure>
</div>

<p style="text-align: center;"><strong>p(+)</strong> = (0.01)(0.9) + (0.99)(0.1) = 0.108</p>
We now know from previous example,

p(C and +) = p(+) . p(C/+)

Thus,

$p(\text {C/+}) = \frac{p(\text{C and +})}{p(\text{+})}= \frac{0.009}{0.108} = 0.0833$

Thus, the probability of a person having cancer, given the test is positive, is 0.0833 or $8.3$ which also conforms with the answer in Udacity.

Summarizing, with single approach we are able to solve both cases, as intuitive as possible (hopefully), even when the methods handled in both cases by respective platforms are not fully clear.

<strong>Note</strong>: I have not yet gotten in to generalized formula and leaving that to readers'. Specifically in above examples, the denominator probability, that is <strong>p(H)</strong> in former case, or <strong>p(+)</strong> in latter case, is actually summation of those probabilities, so in strict sense, should be prefixed with a summation symbol, and index. For brevity, I stuck to the simple form. Once you start sorting out more examples with this approach, the summation and thus the intuition behind the general formula would become clearer.

General Bayes' formula with summation (inference now left to reader as food for thought):

$$
p(A_{i} \mid B)=\frac{p(B \mid A_{i})p(A_{i})}{{\sum^{n}_{i=1} {p(B|{{A}_{i}})p({{A}_{i}})}}}
$$

