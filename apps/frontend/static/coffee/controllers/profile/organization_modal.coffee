@ProfileOrganizationModalController =
  extends: BaseController
  template: '#profile_organization_modal'
  data: ->
    organization: {}
    errors: {}
  props: ['user']
  computed:
    has_errors: ->
      Object.keys(@errors).length > 0
  methods:
    add: ->
      @errors = Organization.validate @organization

      if not @has_errors
        console.log @user

        @organization.leader = @user.id
        Organization.add @organization

        $('.modal').modal('hide')
