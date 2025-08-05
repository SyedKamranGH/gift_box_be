from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']            
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    # def validate(self, data):
    #     user = User.objects.filter(username=data['username']).first()
    #     if user and user.check_password(data['password']):
    #         return user
    #     raise serializers.ValidationError("Invalid credentials")
    
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    # def validate(self, data):
    #     user = self.context['request'].user
    #     if not user.check_password(data['old_password']):
    #         raise serializers.ValidationError("Old password is not correct")
    #     return data
    
    # def save(self):
    #     user = self.context['request'].user
    #     user.set_password(self.validated_data['new_password'])
    #     user.save()
    
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    # def validate(self, data):
    #     user = User.objects.filter(email=data['email']).first()
    #     if not user:
    #         raise serializers.ValidationError("No user found with this email")
    #     return data
    
    # def save(self):
    #     user = User.objects.get(email=self.validated_data['email'])
    # Logic to send reset password email
    # This could involve generating a token and sending an email with a reset link
    #     pass
    
    
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    otp = serializers.CharField(write_only=True, required=True)
    
    # def validate(self, data):
    #     user = User.objects.filter(email=data['email']).first()
    #     if not user:
    #         raise serializers.ValidationError("No user found with this email")
    #     if not user.check_otp(data['otp']):
    #         raise serializers.ValidationError("Invalid OTP")
    #     return data
    # def save(self):
    #     user = User.objects.get(email=self.validated_data['email'])
    #     user.set_password(self.validated_data['new_password'])
    #     user.save()
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
    
    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.role = validated_data.get('role', instance.role)
    #     instance.save()
    #     return instance