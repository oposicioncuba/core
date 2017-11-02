class @User
  @me: ->
    promise = new Promise (resolve) ->
      $.ajax
        url: '/api/me'
        success: (data) =>
          resolve data

    return promise
