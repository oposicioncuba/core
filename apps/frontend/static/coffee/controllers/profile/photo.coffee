@ProfilePhotoController =
  extends: BaseController
  template: '#profile_photo_tmpl'
  props: ['image']
  data: ->
    image: null
  methods:
    uploadFile: (files) ->
      console.log(files)

    openUploadWindow: ->
      $('input[type=file]').click()
