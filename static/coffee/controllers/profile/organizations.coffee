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
      $('.modal').modal()
