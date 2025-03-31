describe('Fill out form and Check List', () => {
  it('Has filled out the form and checked the list', () => {
    cy.visit('http://127.0.0.1:5000/')
    cy.get('input[name="name"]').type('Snowy Thompson', {delay: 100}) //create camper
    cy.get('input[name="age"]').type('12')
    cy.get('input[name="number"]').type('601-630-8004', {delay: 100})
    cy.get('input[name="email"]').type('clevelandfan13@gmail.com', {delay: 100})
    cy.get('input[name="address"]').type('123 Virgo Rd, Calabasas, LA, CA 90210', {delay: 100})
    cy.get('input[name="tshirt"]').type('Extra Small', {delay: 100})
    cy.get('form').submit()
    cy.get('a[href="/list"]').click()
    cy.get('a[href="/delete"]').click() 
    cy.get('input[name]').type('snowy thompson')//assuring that this is case sensetive
    cy.get('form').submit()
    cy.get('a[href="/"]').click()
  })
})