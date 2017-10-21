def verify(function, inputs, outputs):
    for sample_input, expected_output in zip(inputs, outputs):
        actual_output = function(sample_input)
        try:
            assert actual_output == expected_output
        except AssertionError:
            print(
                (
                    "Something seems to be wrong with your code! On the input:\n{}\n"
                    "it should have returned:\n{}\nbut returned:\n{}\n instead!"
                ).format(sample_input, expected_output, actual_output)
            )
    


#############################
#### email_scraper tests ####
#############################


from scraper import find_emails


sample_inputs = [
    """
    This is a long string
    without an email address
    It is what it is
    """,


    """
    This string has an email!
    karl@erik.no
    (don't expect replies!)
    """,
    
    """
    Here is an email:simon@funke.no. It's probably not going to work.
    You could try funsim@uio.no, but I don't think that's the right one either. 
    """,

    """
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>

        
          
            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
            </div>
    """,

    """This is text which contains some email-like strings which aren't emails 
    according to the definition of the assignment:
    the string name@server.1o has a number at the start of thedomain,
    the string name@server.o1 has a number at the end,
    the string name@ser<ver.domin has an illegal character in its server,
    as does the string name@ser"ver.domain,

    however, the string na&me@domain.com is actually an email!
    as is n~ame@dom_ain.com
    but name@domain._com is bad
    (name@domain.c_o.uk is allowed though)
    """
]

expected_outputs = [
    [],
    ["karl@erik.no"],
    ["simon@funke.no", "funsim@uio.no"],
    ["karleh@ifi.uio.no", "karleh@ifi.uio.no"],
    ["na&me@domain.com", "n~ame@dom_ain.com", "name@domain.c_o.uk"]
    
]


verify(find_emails, sample_inputs, expected_outputs)
        
#############################
####  url_scraper tests  ####
#############################

from scraper import find_hyperlinks

sample_inputs = [
    """
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>

        
          
            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
            </div>

    This URL is not inside a hyperlink tag, so should be ignored: "http://www.google.com"
    """,
    
    """
    This is almost a hyperlink, but the quotes are mismatched, so it shouldn't be captured:

    <a href="http://www.google.com/super_secret/all_the_user_data/'>Please don't click</a>

    <a href="http://www.google.com/super_secret/user_data/'>Please don't click</a>


    
    """,

    
]

expected_outputs = [
    [
        "http://www.mn.uio.no/ifi/personer/vit/karleh/index.html",
    ],
    
    []
    
]

verify(find_hyperlinks, sample_inputs, expected_outputs)


################################
####  parse_nwodkram tests  ####
################################

from parser import parse_nwodkram



sample_input = r"""
This is some Nwodkram text. Note that *this* is in italic, and %this% is in bold.
If you want to write an \* or an equal sign and not have the parser eat them, 
that's easy -  note that \* this \* is not in italic even though it's between two \*s,
and \% this \% is not in bold.

[here](www.google.com) is a hyperlink.
[here](http://www.google.com) is another.
[and here](https://www.weird?$|site.weird/path/) is a third with some weird characters.
Follow it at your own peril.

Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
But don't worry too much if some weird combination is ambiguous or results in
weird stuff.
"""

    




expected_output = r"""
This is some Nwodkram text. Note that <i>this</i> is in italic, and <b>this</b> is in bold.
If you want to write an * or an equal sign and not have the parser eat them, 
that's easy -  note that * this * is not in italic even though it's between two *s,
and % this % is not in bold.

<a href='http://www.google.com'>here</a> is a hyperlink.
<a href='http://www.google.com'>here</a> is another.
<a href='https://www.weird?$|site.weird/path/'>and here</a> is a third with some weird characters.
Follow it at your own peril.

Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
But don't worry too much if some weird combination is ambiguous or results in
weird stuff.
"""
verify(parse_nwodkram, [sample_input], [expected_output])
