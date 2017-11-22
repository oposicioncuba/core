@ProfileOrganizationsController =
  extends: BaseController
  template: '#profile_organizations_tmpl'
  props: [
    'user'
  ]
  computed:
    organizations: ->
      @user.organizations
  components:
    'profile_organization': ProfileOrganizationController
    'profile_organization_modal': ProfileOrganizationModalController
  methods:
    openModal: ->
      @$refs.modal.operation = 'Add'
      @$refs.modal.organization = {}
      $('.modal').modal()
    loadOrganization: (organization) ->
      @$refs.modal.operation = 'Update'
      @$refs.modal.organization = organization
      $('.modal').modal()
    reloadUser: ->
      console.log 234

      @$emit 'reloadUser'
