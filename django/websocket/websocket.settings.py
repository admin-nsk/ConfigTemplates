CHANNELS_REDIS_HOST = env.str('CHANNELS_REDIS_HOST', 'localhost')
CHANNELS_REDIS_PORT = env.int('CHANNELS_REDIS_PORT', 6379)

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [f"redis://{CHANNELS_REDIS_HOST}:{CHANNELS_REDIS_PORT}/3"],
        },
    },
}