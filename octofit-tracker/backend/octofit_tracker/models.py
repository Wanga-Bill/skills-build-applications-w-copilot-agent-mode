from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField('User')  # Corrected to ManyToManyField

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.type} - {self.user.email}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.points} points"

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name
