class JobStatusMixin(object):
    STATUS_DRAFT = 'DRAFT'
    STATUS_ACTIVE = 'ACTIVE'
    STATUS_INACTIVE = 'INACTIVE'

    CHOICES_STATUS = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive'),
    )
