load('ext://pack', 'pack')

docker_build(
    'posture-police_api',
    context='.',
    live_update=[
        sync('app/', '/code/app'),
    ],
)

docker_compose('./docker-compose.yml')
