from django import forms
from .models import Todo, Reply


class TodoForm(forms.ModelForm):
    # 日付と日時の入力欄を分ける処理
    deadline = forms.SplitDateTimeField(
        label='締め切り',
        required=False,
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'})
    )

    class Meta:
        model = Todo
        fields = ('title', 'status', 'category', 'deadline', 'content')
        exclude = ('created_at', 'updated_at',)


class TodoUpdateForm(forms.ModelForm):
    # 日付と日時の入力欄を分ける処理
    deadline = forms.SplitDateTimeField(
        label='締め切り',
        required=False,
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'})
    )

    class Meta:
        model = Todo
        fields = ('title', 'status', 'category', 'deadline', 'content')


class TodoSearchForm(forms.Form):
    keyword = forms.CharField(
        label='キーワード', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'キーワードで検索します'})
    )


# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields = ('comment', 'created_at')
class ReplyForm2(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('comment',)
