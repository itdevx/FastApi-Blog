from fastapi  import APIRouter

router = APIRouter()


@router.post('/register')
async def register():
    ...


@router.post('/login')
async def login():
    ...


@router.get('/user-profile')
async def get_user_profile():
    ...


@router.put('/update-profile')
async def user_update_profile():
    ...