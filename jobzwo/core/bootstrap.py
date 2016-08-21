import structlog

def setup_structlog():
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            
            structlog.processors.KeyValueRenderer(
                key_order=['event', 'path', 'method', 'logger', 'level',
                           'client_ip', 'request_id', ],
            ),
        ],
        cache_logger_on_first_use=True,
        context_class=structlog.threadlocal.wrap_dict(dict),
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory()
    )
