# Here is one example of the assignments you will see from now on.<div>
</div><div>There are a few new things. One new thing is the first two lines:</div><div>
</div><div><pre><code>class AboutAssignments(unittest.TestCase):
    def test_if_then_else_statement_true_expression(self):</code></pre> 
</div><div>You can safely ignore them, but sometimes the name of the test (on the second line) contains a hint on what to do.</div><div>
</div><div>What is also new is the form of the assert. Before we used a simple assert, like this:</div><div>
</div><div><pre><code>self.assertEqual(result == 12)</code></pre></div><div>
</div><div>We now have a special assert that checks if two things, separated by a comma, are equal:

<pre><code>self.assertEqual(12, result)</code></pre>
</div><div>The basic assignment remains the same, fill in the blank (__) to make to the code work!</div><div>
</div><div>A good strategy is to run the code first, without changing something, and then reading the error message.</div><div>
</div><div><span>You will have notice that the error messages look different now:</span>
</div><div><div><img alt="" src="https://ucarecdn.com/00552908-7f92-45ad-9039-b509e663b81b/" title="Image: https://ucarecdn.com/00552908-7f92-45ad-9039-b509e663b81b/">
</div><div>The first lines may be ignored as before. We read from , line like we were used to.</div><div>
</div><div>It now says:</div><div>
</div><div>AssertionError: '-=&gt; FILL ME IN! &lt;=-' != 'small enough'
</div><div>
</div><div>That means that the assert is comparing '-=&gt; FILL ME IN! &lt;=-' (which is the blank) with 'small enough' which are not the same. And it is your job to fix it!</div>
</div><div>
</div><div>Maybe you have noticed the error messages look different now too:<div><img alt="" src="https://ucarecdn.com/00552908-7f92-45ad-9039-b509e663b81b/">
</div><div>The first lines may be ignored as before. We read from , line like we were used to.</div><div>
</div><div>It now says:</div><div>
</div><div>AssertionError: '-=&gt; FILL ME IN! &lt;=-' != 'small enough'
</div><div>
</div><div>That means that the assert is comparing '-=&gt; FILL ME IN! &lt;=-' (which is the blank) with 'small enough' which are not the same. And it is your job to fix it!</div>
</div>
class AboutAssignments(unittest.TestCase):
    def test_if_then_else_statement_true_expression(self):
        threshold = 12
        if 5 < threshold:
            result = 'small enough'
        else:
            result = 'too big!'
        self.assertEqual(__, result)