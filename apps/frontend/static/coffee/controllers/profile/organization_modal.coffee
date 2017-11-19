@ProfileOrganizationModalController =
  extends: BaseController
  template: '#profile_organization_modal'
  data: ->
    organization: {}
    errors: {}
  props: ['user']
  computed:
    has_errors: ->
      console.log @errors
      Object.keys(JSON.stringify @errors).length > 0
  methods:
    add: ->
      @errors = Organization.validate @organization

      if not @has_errors
        @organization.leader = @user.id
        Organization.add(@organization).then (data) =>
          Organization.addMemberToOrganization(data.id, @user.id).then ->
            $('.modal').modal('hide')
            @emit('reloadUser')
        .catch (error) =>
          @errors['headquarter'] = error['headquarter'][0]
