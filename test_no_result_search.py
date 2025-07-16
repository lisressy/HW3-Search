from selene import browser
from selene import be, have

def test_search_selene(browser_window_size):
    #browser.open('https://startpage.com')
    browser.element('input[id="q"]').should(be.blank).type('selene').press_enter()
    browser.element('html').should(have.text('Web results'))

def test_search_random_prase(browser_window_size):
    #browser.open('https://startpage.com')
    browser.element('input[id="q"]').should(be.blank).type('paf;dgkl;s;saawfsedf').press_enter()
    browser.element('html').should(have.text('Uh-oh, there are no results for this search.'))