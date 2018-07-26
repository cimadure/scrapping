import unittest

from scrapy import Selector

from viewscount.viewscount.spiders.infinity import InfinityknowSpider


doc = """
 <div>
     <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
 """

doc2 = """
<article id="post-1700" class="post-item clearfix post-1700 post type-post status-publish format-standard hentry category-asp-net category-technology tag-difference-between-value-type-and-reference-type-in-c-code-project tag-heap-memory-meaning tag-how-objects-are-stored-in-memory-in-c tag-memory-allocation-in-c tag-stack-and-heap-in-c-msdn tag-stack-vs-heap-data-structure tag-stack-vs-queue-vs-heap tag-why-objects-are-stored-in-heap-in-c" itemtype="http://schema.org/BlogPosting" itemscope="itemscope">
				<div class="post-item-desc">
			<header class="entry-header">
				<h2 class="entry-title" itemprop="headline"><a href="http://infinityknow.com/difference-between-stack-and-heap-memory-in-c-net/" rel="bookmark">Difference between Stack and Heap memory in C#.NET</a></h2>			</header><!-- .entry-header -->

			<div class="entry-content">
				<p>Difference between Stack and Heap memory in C#.NET Today, We want to share with you Difference between Stack and Heap memory in C#.NET. In this post we will show you Six important .NET concepts: Stack, heap, value types, reference types, hear for Difference between Stack and Heap memory in C# we will give you demo&#8230;</p>
				
			</div><!-- .entry-content -->
		</div>
	</article><!-- #post-## -->
"""

article = """

<div style="clear:both; margin-top:0em; margin-bottom:1em;"><a href="http://infinityknow.com/vuejs-autocomplete-using-laravel-example/" target="_blank" rel="nofollow" class="ub00f9c630928f1c38505b53a70affec8"><!-- INLINE RELATED POSTS 2/3 //--><style> .ub00f9c630928f1c38505b53a70affec8 { padding:0px; margin: 0; padding-top:1em!important; padding-bottom:1em!important; width:100%; display: block; font-weight:bold; background-color:inherit; border:0!important; border-left:4px solid #16A085!important; text-decoration:none; } .ub00f9c630928f1c38505b53a70affec8:active, .ub00f9c630928f1c38505b53a70affec8:hover { opacity: 1; transition: opacity 250ms; webkit-transition: opacity 250ms; text-decoration:none; } .ub00f9c630928f1c38505b53a70affec8 { transition: background-color 250ms; webkit-transition: background-color 250ms; opacity: 1; transition: opacity 250ms; webkit-transition: opacity 250ms; } .ub00f9c630928f1c38505b53a70affec8 .ctaText { font-weight:bold; color:#2980B9; text-decoration:none; font-size: 16px; } .ub00f9c630928f1c38505b53a70affec8 .postTitle { color:#D35400; text-decoration: underline!important; font-size: 16px; } .ub00f9c630928f1c38505b53a70affec8:hover .postTitle { text-decoration: underline!important; } </style><div style="padding-left:1em; padding-right:1em;"><span class="ctaText">READ :</span>&nbsp; <span class="postTitle">VueJs Autocomplete using Laravel Example</span></div></a></div><p></p><div class="ads-banner-block below-single-ads "><script async="" src="article_files/adsbygoogle.js"></script>
<!-- responsive -->
<ins class="adsbygoogle" style="display: block; height: 59px;" data-ad-client="ca-pub-1944225715659599" data-ad-slot="1996366350" data-ad-format="auto" data-full-width-responsive="true" data-adsbygoogle-status="done"><ins id="aswift_4_expand" style="display: inline-table; border: medium none; height: 59px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 640px; background-color: transparent;"><ins id="aswift_4_anchor" style="display: block; border: medium none; height: 59px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 640px; background-color: transparent; overflow: hidden;"><iframe marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_4" name="aswift_4" style="left:0;position:absolute;top:0;width:640px;height:60px;" width="640" height="60" frameborder="0"></iframe></ins></ins></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div><div class="post-views post-1635 entry-meta">
			<span class="post-views-icon dashicons dashicons-chart-bar"></span>
			<span class="post-views-label">Post Views: </span>
			<span class="post-views-count">68</span>
			</div><div class="code-block code-block-5" style="margin: 8px 0; clear: both;">
<script async="" src="article_files/adsbygoogle.js"></script>
<ins class="adsbygoogle" style="display: block; height: 384px;" data-ad-format="autorelaxed" data-ad-client="ca-pub-1944225715659599" data-ad-slot="7479448669" data-adsbygoogle-status="done"><ins id="aswift_5_expand" style="display:inline-table;border:none;height:384px;margin:0;padding:0;position:relative;visibility:visible;width:640px;background-color:transparent;"><ins id="aswift_5_anchor" style="display:block;border:none;height:384px;margin:0;padding:0;position:relative;visibility:visible;width:640px;background-color:transparent;"><iframe marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_5" name="aswift_5" style="left:0;position:absolute;top:0;width:640px;height:384px;" width="640" height="384" frameborder="0"></iframe></ins></ins></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
	"""

header = """
	<header class="entry-header">
		
		<h1 class="entry-title" itemprop="headline">convert generic list to datatable in Asp.Net C#,VB</h1>			<div class="entry-meta">
				<span class="byline">By <span class="author vcard"><a class="url fn n" href="http://infinityknow.com/author/admin/">admin</a></span>&nbsp;</span><span class="posted-on"> On <a href="http://infinityknow.com/convert-generic-list-to-datatable-in-asp-net-cvb/" rel="bookmark"><time class="meta entry-date published updated" itemprop="datePublished" datetime="2018-07-21T04:57:18+00:00">July 21, 2018</time></a>&nbsp;</span><span class="cat-links">In <a href="http://infinityknow.com/technology/asp-net/" rel="category tag">Asp.Net</a>, <a href="http://infinityknow.com/technology/" rel="category tag">Technology</a>&nbsp;</span><span class="tags-links">Tagged <a href="http://infinityknow.com/tag/convert-list-to-dataset-in-asp-net/" rel="tag">convert list to dataset in asp net</a>, <a href="http://infinityknow.com/tag/convert-list-to-dataset-in-mvc/" rel="tag">convert list to dataset in mvc</a>, <a href="http://infinityknow.com/tag/convert-list-to-datatable-in-c-extension-methods/" rel="tag">convert list to datatable in c# extension methods</a>, <a href="http://infinityknow.com/tag/convert-list-to-datatable-in-c-using-linq/" rel="tag">convert list to datatable in c# using linq</a>, <a href="http://infinityknow.com/tag/convert-list-to-datatable-in-c-without-looping/" rel="tag">convert list to datatable in c# without looping</a>, <a href="http://infinityknow.com/tag/convert-nested-list-to-datatable-in-c/" rel="tag">convert nested list to datatable in c#</a>, <a href="http://infinityknow.com/tag/how-to-convert-model-to-datatable-in-c/" rel="tag">how to convert model to datatable in c#</a>, <a href="http://infinityknow.com/tag/vb-net-list-to-datatable/" rel="tag">vb.net list to datatable</a>&nbsp;</span><span class="comments-link"><a href="http://infinityknow.com/convert-generic-list-to-datatable-in-asp-net-cvb/#respond">Leave a comment&nbsp;</a></span>			</div><!-- .entry-meta -->		
		<div class="floating-to-right sharing-top-float">		<div class="superads-social-sharing social-sharing-left">
		<ul class="superads-social-icons">
			
			<li class="facebook">
				<a href="https://www.facebook.com/sharer/sharer.php?u=http://infinityknow.com/convert-generic-list-to-datatable-in-asp-net-cvb/" class="social-popup">
					<i class="fa fa-facebook-square"></i>
			        <span class="text">facebook</span>
				</a>
			</li>
			
			<li class="twitter">
				<a href="http://twitter.com/share?url=http://infinityknow.com/convert-generic-list-to-datatable-in-asp-net-cvb/&amp;text=convert%20generic%20list%20to%20datatable%20in%20Asp.Net%20C#,VB" class="social-popup">
					<i class="fa fa-twitter"></i>
			        <span class="text">tweet</span>
				</a>
			</li> 
			
			<li class="googleplus">
				<a href="https://plus.google.com/share?url=http://infinityknow.com/convert-generic-list-to-datatable-in-asp-net-cvb/" class="social-popup">
					<i class="fa fa-google-plus"></i>
			        <span class="text">google+</span>
				</a>
			</li>
			
		</ul>
		</div>
		</div>
	</header><!-- .entry-header -->
"""


class TestArticleItemPage(unittest.TestCase):
    def setUp(self):
        self.selector = Selector(text=doc2, type="html")

    def test_url_extraction(self):
        self.assertEqual('http://infinityknow.com/difference-between-stack-and-heap-memory-in-c-net/',
                         InfinityknowSpider._get_url(self.selector))

    def test_article_id(self):
        self.assertEqual("post-1700", InfinityknowSpider._get_id(self.selector))

    def test_article_title(self):
        self.assertEqual("Difference between Stack and Heap memory in C#.NET",
                         InfinityknowSpider._get_title(self.selector))


class TestArticle(unittest.TestCase):
    def setUp(self):
        self.selector = Selector(text=article, type="html")

    def test_views_count(self):
        self.assertEqual('68',
                         InfinityknowSpider._get_view_count(self.selector))


class TestArticleCategory(unittest.TestCase):
    def setUp(self):
        self.selector = Selector(text=header, type="html")

    def test_article_categories(self):
        self.assertEqual(['Asp.Net', 'Technology'],
                         InfinityknowSpider._get_category(self.selector))
