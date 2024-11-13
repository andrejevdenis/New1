from selene import browser, be, have


browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('налог ру').press_enter()
browser.element('[id="search"]').should(have.text('Федеральная налоговая служба'))