class @Organization
  @validate: (organization) ->
    errors = {}

    fields = ['name', 'description', 'headquarter']

    for field in fields
      if not organization[field]
        errors[field] = 'This field is required'

    errors

  @add: (organization) ->
    promise = new Promise (resolve, reject) ->
      $.ajax
        url: '/api/organizations/'
        method: 'post'
        data: organization
        success: (data) =>
          resolve data
        error: (xhr) =>
          reject xhr.responseJSON

    promise

  @addMemberToOrganization: (organizationId, userId) ->
    promise = new Promise (resolve) ->
      $.ajax
        url: '/api/organizationmembers/'
        method: 'post'
        data:
          member: userId
          organization: organizationId
          leader: true
        success: (data) ->
          resolve data

    promise
