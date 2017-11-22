@ProfileOrganizationController =
  extends: BaseController
  template: '#organization_tmpl'
  props: [
    'organization',
  ]
  methods:
    edit: ->
      @$emit 'loadOrganization', @organization

    remove: (organization) ->
      swal
        title: 'Are you sure?'
        text: "This action can't be restored"
        showCancelButton: true
      .then (result) =>
        if result.value
          Organization.remove(organization).then =>
            @emit 'reloadUser'


