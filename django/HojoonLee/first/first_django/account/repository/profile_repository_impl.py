from account.repository.profile_repository import ProfileRepository
from account.entity.profile import Profile
class ProfileRepositoryImpl(ProfileRepository):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def findByEmail(self, email):
        try:
            profile = Profile.objects.get(email=email) # email과 일치하는 녀석 1개만 가져오기
            return profile
        except Profile.DoesNotExist:
            print(f"이메일로 profile 찾을 수 없음: {email}")
            return None
        except Exception as e:
            print(f"이메일 중복 검사 중 에러 발생: {e}")
            return None