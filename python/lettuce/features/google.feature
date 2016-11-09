Feature: Authentication
  In order to protect private information
  As a registered user
  I want to log in to my Google admin portal

# Scenario: I enter my password correctly
#   Given the user "Suraya" exists with phone number "8049941406"
#   And I am at "https://accounts.google.com/ServiceLogin"
#   When I fill in "Enter your email" with "sraya16@vt.edu"
#   And I fill in "Password" with "s3xyb2ck21*"
#   And I press "Sign In"
#   Then I should be at "https://accounts.google.com/signin/newfeatures"
#   And I should see "Some new features for your G" in the tab

Scenario: The Election Google Doodle works as a hyperlink
  Given the Google Doodle's image alt text reads "U.S. Elections 2016: Results Live"
  And I am at "https://www.google.com/"
  When I click on the interactive Google Doodle
  Then I should be at "https://www.google.com/#q=US+election+results"
  And I should see "US election results" in the search bar
  And I should see "US Election Results" in the tab

Scenario Outline: The main search bar works correctly
  Given the search bar is located under the Google Doodle
  And I am at "https://www.google.com/"
  When I type "<keyword>" in the search input
  And I press enter
  Then I should see "<query_url>" + my searched keywords in the search bar

  Examples:
  | keyword | query_url |
  | soccer | https://www.google.com/#q=soccer |
  | football | https://www.google.com/#q=football |

Scenario: The I'm Feeling Lucky CTA button exists
  Given I am at "https://www.google.com/"
  And The I'm Feeling Lucky button is present.
  When I hover over the button with my mouse
  Then I should see text not equal to I'm feeling lucky

Scenario Outline: Voice Search works correctly on Chrome
  Given Google has access to use the computer's microphone
  And I am at "https://www.google.com/"
  When I click on the microphone icon in the search bar
  And I speak clearly in near my computer
  And there is little to no background noise
  Then I should see "https://www.google.com/#q=" + my voice search

  Examples:
  | keyword | query_url |
  | numerology calculator | https://www.google.com/#q=numerology+calculator |
  | average lifespan of cats | https://www.google.com/#q=average+lifespan+of+cats |


# Scenario: The Live Feedback Footnote CTAs work as a hyperlinks
#   Given the "AP", "Learn More", "Feedback" CTAs exist
#   And I am at "https://www.google.com/#q=US+election+results"
#   When I click on the "AP" CTA
#   Then I should be at "http://ap.org/products-services/elections/FAQs"
#   And I should see "Counting the Vote" in the tab
#   When I click on the "Learn More" CTA
#   Then I should be at "https://www.google.com/elections/attribution/"
#   And I should see "Legal Notices for Election" in the tab
