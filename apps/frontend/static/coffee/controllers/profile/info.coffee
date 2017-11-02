@ProfileInfoController =
  extends: BaseController
  template: '#profile_info_tmpl'
  props: [
    'name',
    'last_name',
    'birthday',
    'verified',
  ]