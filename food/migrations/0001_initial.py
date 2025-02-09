# Generated by Django 3.0.8 on 2020-09-13 21:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import food.managers
import food.models
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='last name')),
                ('avatar', models.ImageField(blank=True, default='static/avatars/default.jpg', null=True, upload_to='static/avatars/')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('chef', 'Chef'), ('subscriber', 'Subscriber'), ('doctor', 'Doctor'), ('company', 'Company')], max_length=50, verbose_name='user type')),
                ('is_doctor', models.BooleanField(default=False, verbose_name='doctor')),
                ('is_company', models.BooleanField(default=False, verbose_name='company')),
                ('is_subscriber', models.BooleanField(default=True, verbose_name='subscriber')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', food.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Allergie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=50)),
                ('last_Name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='name')),
                ('barcode', models.CharField(max_length=50, verbose_name='barcode')),
                ('country', models.CharField(max_length=50, verbose_name='country')),
                ('quantity', models.FloatField(default=0.0, verbose_name='quantity')),
                ('image', models.CharField(max_length=200, verbose_name='image')),
                ('ingredients', models.TextField(verbose_name='ingredients')),
                ('ingredients_image', models.CharField(max_length=200, verbose_name='ingredients image')),
                ('nutrition_image', models.CharField(max_length=200, verbose_name='nutrition image')),
                ('nutrition_score', models.FloatField(default=0.0, verbose_name='nutrition score')),
                ('nutrition_grade', models.CharField(max_length=50, verbose_name='nutrition grade')),
                ('energy', models.FloatField(default=0.0, verbose_name='energy kj')),
                ('lipids', models.FloatField(default=0.0, verbose_name='lipids')),
                ('fat', models.FloatField(default=0.0, verbose_name='fat')),
                ('saturated_fat', models.FloatField(default=0.0, verbose_name='saturated fat')),
                ('carbohydrates', models.FloatField(default=0.0, verbose_name='carbohydrates')),
                ('sugar', models.FloatField(default=0.0, verbose_name='sugar')),
                ('fiber', models.FloatField(default=0.0, verbose_name='fiber')),
                ('protein', models.FloatField(default=0.0, verbose_name='protein')),
                ('salt', models.FloatField(default=0.0, verbose_name='salt')),
                ('sodium', models.FloatField(default=0.0, verbose_name='sodium')),
                ('additives', models.CharField(default='', max_length=50, verbose_name='additives')),
                ('tags', models.CharField(default='', max_length=50, verbose_name='tags')),
                ('accepted', models.BooleanField(default=False, verbose_name='accepted')),
                ('allergy', models.CharField(default='no allergy', max_length=100, verbose_name='allergy')),
            ],
        ),
        migrations.CreateModel(
            name='health_problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('authorized', 'Authorized'), ('captured', 'Captured'), ('cancelled', 'Cancelled'), ('refunded', 'Refunded')], max_length=50, verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='title')),
                ('blog_type', models.CharField(choices=[('audio', 'Audio'), ('video', 'Video'), ('quote', 'Text'), ('image', 'Image'), ('link', 'Link')], max_length=50, verbose_name='blog type')),
                ('tags', models.CharField(max_length=200, verbose_name='tags')),
                ('categories', models.CharField(max_length=200, verbose_name='categories')),
                ('content', tinymce.models.HTMLField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/posts/')),
                ('likes', models.IntegerField(default=0, verbose_name='likes')),
                ('dislikes', models.IntegerField(default=0, verbose_name='dislikes')),
                ('bgcolor', models.CharField(choices=[('white', '#ffffff'), ('green', '#21ba45'), ('pink', '#e03997'), ('blue', '#2185d0'), ('teal', '#00b5ad'), ('red', '#db2828'), ('olive', '#b5cc18'), ('orange', '#f2711c'), ('yellow', '#fbbd08'), ('violet', '#6435c9'), ('purple', '#a333c8')], default='white', max_length=50, verbose_name='bg color')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='puser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('recommender', models.CharField(max_length=100, verbose_name='recommender')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('created', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='static/products/')),
                ('ingredients', models.TextField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Categorie')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('tags', models.CharField(default='notags', max_length=200, verbose_name='tags')),
                ('preparation', tinymce.models.HTMLField()),
                ('ingredients', tinymce.models.HTMLField()),
                ('image_url', models.URLField(max_length=220, verbose_name='image')),
                ('likes', models.IntegerField(default=0, verbose_name='likes')),
                ('dislikes', models.IntegerField(default=0, verbose_name='dislikes')),
                ('sugar', models.FloatField(default=0.0)),
                ('carbohydrates', models.FloatField(default=0.0)),
                ('fat', models.FloatField(default=0.0)),
                ('lipides', models.FloatField(default=0.0)),
                ('sodium', models.FloatField(default=0.0)),
                ('glucides', models.FloatField(default=0.0)),
                ('proteines', models.FloatField(default=0.0)),
                ('vitamine_d', models.FloatField(default=0.0)),
                ('vitamine_e', models.FloatField(default=0.0)),
                ('vitamine_c', models.FloatField(default=0.0)),
                ('vitamine_b1', models.FloatField(default=0.0)),
                ('calcium', models.FloatField(default=0.0)),
                ('iron', models.FloatField(default=0.0)),
                ('saturated_fat', models.FloatField(default=0.0)),
                ('energy', models.FloatField(default=0.0)),
                ('fiber', models.FloatField(default=0.0)),
                ('cholesterol', models.FloatField(default=0.0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('accepted', models.BooleanField(default=False)),
                ('cuisine', models.CharField(choices=[('african', 'African'), ('asian', 'Asian'), ('european', 'European'), ('tunisian', 'Tunisian')], default='tunisian', max_length=40, verbose_name='cuisine')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Categorie')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40, null=True, verbose_name='author')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email')),
                ('website', models.CharField(max_length=100, null=True, verbose_name='website')),
                ('content', models.TextField(null=True, verbose_name='content')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='created')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_comment', to='food.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('specialty', models.CharField(max_length=50, verbose_name='specialty')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('birthday', models.DateField(auto_now_add=True, verbose_name='birthday')),
                ('phone', models.CharField(max_length=40, verbose_name='phone')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100, verbose_name='enterprise name')),
                ('eid', models.CharField(max_length=150, verbose_name='enterprise identifier')),
                ('domain', models.CharField(max_length=100, verbose_name='work domain')),
                ('phone', models.CharField(max_length=30, verbose_name='phone')),
                ('fax', models.CharField(max_length=30, verbose_name='fax')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRating',
            fields=[
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='food.Recipe')),
                ('rating', models.CharField(choices=[(1, 'Bad'), (2, 'meh'), (3, 'OK'), (4, 'Good'), (5, 'Delicious')], max_length=50, verbose_name='rating')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=50, null=True, verbose_name='gender')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='address')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='phone')),
                ('allergy', models.CharField(blank=True, max_length=150, null=True, verbose_name='allergy')),
                ('health', models.CharField(blank=True, max_length=150, null=True, verbose_name='health')),
                ('weight', models.FloatField(blank=True, default=0.0, null=True, verbose_name='weight')),
                ('height', models.FloatField(blank=True, default=0.0, null=True, verbose_name='height')),
                ('blood_type', models.CharField(blank=True, choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=50, null=True, verbose_name='blood type')),
                ('activity_level', models.CharField(default='sedentary', max_length=40, verbose_name='activity level')),
                ('diet_type', models.CharField(default='muslim', max_length=40, verbose_name='diet type')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_replies', to='food.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeCommentReplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True, verbose_name='content')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='created')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_replay', to='food.RecipeComment')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replay_author', to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_comment_reply', to='food.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabe', models.BooleanField(default=False, verbose_name='available')),
                ('calories_energy', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('lipid_energy', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('fat', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('saturated_fat', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('sodium', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('salt', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('glucides', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('sugar', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('protein', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('calcium', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('iron', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('fiber', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('usage', models.CharField(max_length=250, verbose_name='usage')),
                ('properties', models.CharField(max_length=250, verbose_name='properties')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('sweet', 'Sweet snacks'), ('fruits', 'Fruit Vegetebales'), ('savoury', 'Savoury Snacks'), ('milk', 'Milk and Milk products'), ('sauces', 'Bold and Sauces'), ('cereals', 'Cereal and Cereal Products'), ('fish', 'Fish Meat and Eggs'), ('beverages', 'Beverages')], max_length=50, verbose_name='category')),
                ('products', models.ManyToManyField(to='food.CustomerProduct')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderline_uid', models.CharField(default=food.models.generate_uid_string, max_length=100, unique=True, verbose_name='order line uid')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(default=food.models.generate_uid_string, max_length=100, verbose_name='order number')),
                ('status', models.CharField(choices=[('processing', 'Processing'), ('shipped', 'Shipped'), ('failed', 'Failed'), ('returned', 'Returned')], default='processing', max_length=50, verbose_name='status')),
                ('ordered', models.BooleanField(default=False)),
                ('payment', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('delivery_address', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('orderlines', models.ManyToManyField(to='food.OrderLine')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='subject')),
                ('content', models.TextField(verbose_name='message')),
                ('sent', models.DateTimeField(auto_now=True, verbose_name='sent')),
                ('seen', models.BooleanField(default=False, verbose_name='seen')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Educate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('title_arabe', models.CharField(max_length=100, verbose_name='title arabe')),
                ('description', models.TextField(verbose_name='description')),
                ('description_arabe', models.TextField(verbose_name='description arabe')),
                ('source', models.CharField(max_length=60, verbose_name='source')),
                ('educate_type', models.CharField(choices=[('constipation', 'Constipation'), ('all', 'Nutrition for babies'), ('allergy', 'Allergy'), ('obesity', 'Obesity'), ('diabete', 'Diabete'), ('sport', 'Sport'), ('pregnant', 'Pregnant women nutrition')], max_length=30, verbose_name='type')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/educate/')),
                ('createdAt', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerHealth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name='amount')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.CustomerProduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='O+', max_length=10)),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('height', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('allergicProblem', models.ManyToManyField(to='food.Allergie', verbose_name='list of allergies')),
                ('health_problem', models.ManyToManyField(to='food.health_problem', verbose_name='list of health_problems')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='timestamp')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.CustomerProduct')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='author')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('website', models.CharField(max_length=100, verbose_name='website')),
                ('content', models.TextField(verbose_name='content')),
                ('created', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpost', to='food.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('Description', models.TextField()),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='sattic/blog/images/')),
                ('video', models.FileField(upload_to='static/blog/videos/')),
                ('tags', models.CharField(max_length=100)),
                ('Categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Categorie')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
