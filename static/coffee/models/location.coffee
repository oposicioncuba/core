class @Location
  @get: (id) ->
    promise = new Promise (resolve) =>
      $.ajax
          url: "/api/locations/#{id}"
          success: (data) =>
            resolve data

    promise
