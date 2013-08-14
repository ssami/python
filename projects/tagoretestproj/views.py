        		try:
                    resourceType = form.cleaned_data['resourceType']
                    if resourceType =="Activity":
                        activity = Activity()
                        activity.title = form.cleaned_data['title']
                        activity.lesson = form.cleaned_data['lesson']
                        activity.goals = form.cleaned_data['goals']
                        activity.materials = form.cleaned_data['materials']
                        activity.author = request.user
                        activity.save()
                        activity.chapters.add(form.cleaned_data['chapter'])
                        if request.FILES:
                            attachments = request.FILES.getlist('attachment')
                        try:
                            if attachments:
                                for attach in attachments:
                                    file = File.objects.create(title=attach.name, doc=attach)
                                    activity.files.add(file)
                                    activity.save()
                        except:
                            activity.save()
                    
                    else:
                        project = Project()
                        project.title = form.cleaned_data['title']
                        project.instructions = form.cleaned_data['lesson']
                        project.goals = form.cleaned_data['goals']
                        project.materials = form.cleaned_data['materials']
                        project.author = request.user
                        project.save()
                        project.chapters.add(form.cleaned_data['chapter'])
                        if request.FILES:
                            attachments = request.FILES.getlist('attachment')
                        try:
                            if attachments:
                                for attach in attachments:
                                    file = File.objects.create(title=attach.name, doc=attach)
                                    project.files.add(file)
                                    project.save()
                        except:
                            project.save()
