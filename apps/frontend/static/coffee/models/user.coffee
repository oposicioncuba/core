class @User
  @id: null

  @me: ->
    promise = new Promise (resolve) =>
      $.ajax
        url: '/api/me'
        success: (data) =>
          @id = data[0].id
          resolve data

    promise

  @updatePhoto: (photo) ->
    data = new FormData()
    data.append 'photo', photo

    promise = new Promise (resolve) =>
      $.ajax
        url: "/api/me/#{@id}/"
        data: data
        method: 'put'
        cache: false
        contentType: false
        processData: false
        success: (data) =>
          resolve data

    promise
  @updateInfo: (id, name, last_name, birthday, verified) ->
      promise = new Promise (resolve) =>
        $.ajax
          url: "/api/me/#{id}/"
          data:
            name: name
            last_name: last_name
            birthday: birthday
            verified: verified
          method: 'put'
          success: (data) =>
            resolve data

      promise

  @updateLocation: (locationId) ->
    promise = new Promise (resolve) =>
      $.ajax
        url: "/api/me/#{@id}/address/"
        data:
          location: locationId
        method: 'put'
        success: (data) =>
          resolve data

    promise
