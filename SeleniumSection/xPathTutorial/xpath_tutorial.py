"""
// --> RELATIVE XPATH
/  --> ABSOLUTE XPATH

FORMAT:
    //tag[@attribute='value']
    //*[@attribute='value'] --> Any tag that has the *attribute*
"""

# cart typed in console by me --> //ul[@id="site-header-cart"]
# cart generated in console ----> //*[@id="site-header-cart"]

# cart absolute xPath ----------> /html/body/div[2]/header/div[2]/div/ul --> !!! Absolute xPath easy to brake, better use the relative path !!!

# CONTAINS: can be used to search for the same --> //ul[contains(@id, "site")] = same result as //ul[@id="site-header-cart"]

# text(): Find by the text in te web --> //a[text()="Lost your password?"]

### contains + text() ###
#Combination ----> //a[contains(text(), "Lost")]