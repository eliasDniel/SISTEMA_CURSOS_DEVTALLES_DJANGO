from django.shortcuts import render

# Create your views here.
def courses_list(request):
    courses = [
        {
            'id': 1,
            'level': 'Beginner',
            'rating': 4.5,
            'course_title': 'Introduction to Python',
            'instructor': 'John Doe',
            'course_image': 'images/curso_1.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/42.jpg',
        },

        {
            'id': 2,
            'level': 'Intermediate',
            'rating': 4.7,
            'course_title': 'Web Development with Django',
            'instructor': 'Jane Smith',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/45.jpg',
        },
        {
            'id': 3,
            'level': 'Advanced',
            'rating': 4.9,
            'course_title': 'Data Science with Python',
            'instructor': 'Alice Johnson',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/48.jpg',
        },
        {
            'id': 4,
            'level': 'Beginner',
            'rating': 4.6,
            'course_title': 'JavaScript Essentials',
            'instructor': 'Bob Brown',
            'course_image': 'images/curso_4.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/50.jpg',
        },

    ]
    return render(request, 'courses/courses.html', {'courses': courses})
def courses_detail(request):
    course = {
        'course_title': 'Introduction to Python',
        'course_link': 'courses_leasson',
        'course_image': 'images/curso_2.jpg',
        'info_course': {
            'leassons': 10,
            'duration': '5 hours',
            'instructor': 'John Doe',
        },
        'course_content': [
            {
                'id': 1,
                'name': 'Getting Started with Python',
                'leassons': [
                        {
                            'name': '¿Que aprendereas en este curso?',
                            'type': 'video',
                        },
                    {
                            'name': 'Instalacion de Python',
                            'type': 'article',
                        },
                    
                ], }

        ],
    }

    return render(request, 'courses/courses_detail.html', {'course': course})


def courses_leasson(request):
    leasson = {
            'course_title': 'Introduction to Python',
            'progress': 30,
            'course_content': [
                {
                    'id': 1,
                    'name': 'Getting Started with Python',
                    'total_leassons': 10,
                    'completed_leassons': 3,
                    'leassons': [
                            {
                                'name': '¿Que aprendereas en este curso?',
                                'type': 'video',
                            },
                        {
                                'name': 'Instalacion de Python',
                                'type': 'article',
                            },
                        
                    ], },
                
                    
    
            ],
        }
    return render(request, 'courses/courses_lessons.html', {'leasson': leasson})
