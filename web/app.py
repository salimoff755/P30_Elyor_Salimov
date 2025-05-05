from starlette.applications import Starlette

from starlette_admin.contrib.sqla import Admin, ModelView

from db import db
from db.models import Customer, Developer, User

app = Starlette()
admin = Admin(engine=db._engine,
              title="P30 Admin",
              base_url= "/")
              # auth_provider=UsernameAndPasswordProvider(),
              # middlewares=[Middleware(SessionMiddleware, secret_key=Env().web.TOKEN)]

admin.add_view(ModelView(Customer))
admin.add_view(ModelView(Developer))
admin.add_view(ModelView(User))

admin.mount_to(app)