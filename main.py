import flet as ft
from flet.auth.providers import GitHubOAuthProvider

GIT_CLIENT_ID = 'Ov23liWsr7wRFeC0HTu6'
GIT_CLIENT_SECRET = "f605ea474edb9555d1b382f1e752ac6119c41311"

# porta -p 61559 

def main(page:ft.Page):
    provider = GitHubOAuthProvider(
        client_id=GIT_CLIENT_ID,
        client_secret=GIT_CLIENT_SECRET,
        redirect_url='http://127.0.0.1:61559/api/oauth/redirect'
    )

    def on_login(e: ft.LoginEvent):
        if not e.error:
            print("Login bem-sucedido")
            import pprint
            pprint.pprint(page.auth.user)
        else:
            print(f"Erro no login: {e.error}")
    
    page.on_login = on_login

    page.add(ft.ElevatedButton(
        text='Login com Github',
        on_click=lambda _: page.login(provider=provider)        
        ))


if __name__ == '__main__':
    ft.app(target=main)