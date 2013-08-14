{% extends 'base.html' %}

<head>

{% comment %}
{{ submit_resource_form.media }}
{% endcomment %}

{% block script %}
<script type="text/javascript" src="/static/tiny_mce/tiny_mce.js"></script>
{% endblock script %}

</head>

{% block content %}

<div class="resourceContent">
        
        {% if "Thank" in message %}
            <span class="label label-success">{{message}}</span>
        {% else %}
            <span class="label label-error">{{message}}</span>
        {% endif %}
        
        {% if submit_resource_form %}
            <form method="POST" action ="." enctype="multipart/form-data" style="padding-left:15px">
                {% csrf_token %}    
                
                <span style="color:#ad1d28">
                    {{ submit_resource_form.non_field_errors }}
                </span>
                <div style="display:table; margin:0 auto;">
                    <div class="formLineElement">
                            <span style="color:#ad1d28">
                                {{ submit_resource_form.curriculum.errors }}
                            </span>
                            <label for="id_curriculum">Curriculum</label>
                            {{ submit_resource_form.curriculum }}
                    </div>
            
                    <div class="formLineElement">
                            <span style="color:#ad1d28">
                                {{ submit_resource_form.subject.errors }}
                            </span>
                            <label for="id_subject">Subject</label>
                            {{ submit_resource_form.subject }}
                    </div>

            
                    <div class="formLineElement">
                            <span style="color:#ad1d28">
                                    {{ submit_resource_form.grade.errors }}
                            </span>
                         <label for="id_grade">Grade</label>
                            {{ submit_resource_form.grade }}
                    </div>

            
                    <div class="formLineElement">
                            <span style="color:#ad1d28">
                                    {{ submit_resource_form.chapter.errors }}
                            </span>
                            <label for="id_chapter">Chapter</label>
                            {{ submit_resource_form.chapter }}
                    </div>
                    
                    <div class="formLineElement">
                            {{ submit_resource_form.title.errors }}
                            <label for="id_title">Activity Title</label>
                            {{ submit_resource_form.title }}
                    </div>
                </div>

                <div style="display:table; margin:0 auto;">
                    <div class="formLineElement">
                            {{ submit_resource_form.lesson.errors }}
                            <label for="id_title">Lesson Details</label>
                            {{ submit_resource_form.lesson }}
                    </div>
                </div>
                
                <div style="display:table; margin:0 auto;">
                    <div class="formLineElement">
                            {{ submit_resource_form.materials.errors }}
                            <label for="id_title">Materials</label>
                            {{ submit_resource_form.materials }}
                    </div>
                </div>
                
                <div style="display:table; margin:0 auto;">
                    <div class="formLineElement">
                            {{ submit_resource_form.goals.errors }}
                            <label for="id_goals">Activity/Project Goals</label>
                            {{ submit_resource_form.goals }}
                    </div>
                </div>
                <div id="attach" style="display:table; margin:0 auto;">
                    <div class="formLineElement">
                            {{ submit_resource.form.attachment.errors }}
                            <label for="id_attachment">Attachment</label>
                            {{ submit_resource_form.attachment }}
                    </div>
                </div>
                <div style="display:table; margin:0 auto;">
                    <div class="formLineElement">
                            <button type="submit" class="btn btn-danger" name="submit"> Submit Resource</button>
                    </div>
                </div>
            </form>
        {% endif %}
        
</div> <!-- resourceContent -->
        <br><br><br>
        
<div class="sideBox">
    <h4>Help build Educator Lab by submitting a resource!</h4>
    <p> Thank you for helping us develop new content at Educator Lab. It's teachers such as yourselves who are responsible for growing and supporting this site, and we appreciate every contribution you make.
    </p>
    <p>Contributing to The Educator Lab is easy.</p>
        <ol><br>
            <li>Complete the form on the left, filling in as many details as possible. Then hit Submit.</li><br>
            <li>Our content editors will try to make simple edits and then publish your content. If the resource needs more detailed edits, editors may get back in touch with you to clarify details.</li>
        </ol>
        <i>Please Note: we cannot guarantee that your resource will appear on our site.</i>

        <p style="padding-bottom: 50px"></p>
</div>
        
{% endblock content %}
        