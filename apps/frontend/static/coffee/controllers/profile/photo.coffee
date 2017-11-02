@ProfilePhotoController =
  extends: BaseController
  template: '#profile_photo_tmpl'
  props: ['image']
  computed:
    image_cp: ->
      @image
  methods:
    uploadFile: (files) ->
      User.updatePhoto(files[0])

    openUploadWindow: ->
      $('input[type=file]').click()
