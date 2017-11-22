@ProfileOrganizationModalController =
  extends: BaseController
  template: '#profile_organization_modal'
  data: ->
    organization: {}
    errors: {}
    operation: ''
  props: ['user']
  computed:
    has_errors: ->
      Object.keys(@errors).length > 0
  methods:
    add: ->
      @errors = Organization.validate @organization

      if not @has_errors
        if not @organization.id
          Organization.add(@organization).then (data) =>
            Organization.addMemberToOrganization(data.id, @user.id).then =>
              $('.modal').modal('hide')
              @$emit('reloadUser')
          .catch (error) =>
            console.log error

            @errors = {
              'headquarter': error['headquarter'][0]
            }
        else
          Organization.update(@organization).then =>
            $('.modal').modal('hide')
            @$emit('reloadUser')
